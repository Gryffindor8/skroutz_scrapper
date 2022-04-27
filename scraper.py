import json
import os.path
import time

import requests
from fake_useragent import UserAgent
from lxml import etree
import xml.etree.ElementTree as ET
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

xmlurl = "https://tripanaki.gr/wp-content/uploads/webexpert-skroutz-xml/skroutz.xml"
mystore = "Tripanaki"


def xml_read(prod, pat):
    try:
        return prod.find(str(pat)).text
    except AttributeError:
        return "-"


p_name, p_cat, p_man, p_mpn, p_image, p_price, = [], [], [], [], [], []


def ReadXml():
    # print("Loading XML...")
    data = requests.get(xmlurl)
    xml_doc = etree.fromstring(data.content)
    products = xml_doc.xpath("//product")
    for product in products:
        p_name.append(xml_read(product, "name"))
        p_cat.append(xml_read(product, "category"))
        p_man.append(xml_read(product, "manufacturer"))
        p_mpn.append(xml_read(product, "mpn"))
        p_image.append(xml_read(product, "image"))
        p_man.append(xml_read(product, "manufacturer"))
    print(p_name)


def acp_api_send_request(driver, message_type, data={}):
    message = {
        # this receiver has to be always set as antiCaptchaPlugin
        'receiver': 'antiCaptchaPlugin',
        # request type, for example setOptions
        'type': message_type,
        # merge with additional data
        **data
    }
    # run JS code in the web page context
    # preceicely we send a standard window.postMessage method
    return driver.execute_script("""
    return window.postMessage({});
    """.format(json.dumps(message)))


def Scrap():
    options = Options()
    # ua = UserAgent()
    # userAgent = ua.random
    # options.add_argument(f'user-agent={userAgent}')
    options.add_extension('anticaptcha-plugin_v0.62.crx')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.maximize_window()
    driver.get("https://www.skroutz.gr/")
    acp_api_send_request(
        driver,
        'setOptions',
        {'options': {'antiCaptchaApiKey': '3cc92dd56f82ead0f09617bd80cdbf06'}}
    )
    # 3 seconds pause
    time.sleep(3)
    driver.get("https://www.skroutz.gr")
    # driver.find_element(By.ID, "accept-all").click()
    ids = 1
    try:
        for product_id, product_name in enumerate(p_name):
            search_bar = WebDriverWait(driver, 180).until(
                EC.presence_of_element_located((By.XPATH, '//input[@id="search-bar-input"]')))
            search_bar.clear()
            search_bar.send_keys(product_name)
            search_bar.send_keys(Keys.RETURN)
            try:
                link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[@class='js-sku-link']")))
            except TimeoutException:
                # time.sleep(1)
                continue
            try:
                page_title = driver.find_element(By.XPATH, "//h1[@class='page-title']")
                # time.sleep(1)
                continue
            except NoSuchElementException:
                # time.sleep(1)
                driver.execute_script("arguments[0].click();", link)
                try:
                    product_cards = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.XPATH, '//li[@class="card js-product-card"]')))
                    # time.sleep(1)
                except TimeoutException:
                    # time.sleep(1)
                    continue
                num_cards = len(product_cards)
                i = 0
                for product_card in product_cards:
                    ActionChains(driver).move_to_element(product_card).perform()
                    try:
                        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
                        wait = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions)
                        store_name = wait.until(lambda d: product_card.find_element(By.CLASS_NAME, "shop-name")).text
                        if store_name == mystore:
                            # flag = 1
                            # if flag == 0 and i >= 4:
                            #     i = i + 1
                            continue
                        price = wait.until(lambda d: product_card.find_element(By.CLASS_NAME, "dominant-price")).text
                        shipping_prices = wait.until(
                            lambda d: product_card.find_elements(By.CSS_SELECTOR, ".extra-cost.cf>em"))
                        shipping = shipping_prices[0].text
                        delivery = shipping_prices[1].text
                        deliver_time = wait.until(
                            lambda d: product_card.find_element(By.CSS_SELECTOR, "span.availability")).text
                    except:
                        continue
                    data_ = [ids, product_id + 1, store_name, str(i + 1), num_cards, price, shipping,
                             delivery,
                             deliver_time]
                    df = pd.DataFrame(data=data_,
                                      index=["id", "product", "storename", "place", "totalnum", "price",
                                             "shipping", "delivery", "availability"]).T
                    df.to_csv("compete.csv", mode='a', header=not (os.path.isfile("compete.csv")), index=False)
                    i = i + 1
                    ids = ids + 1
        print("Scraping completed")
    except:
        pass
    finally:
        driver.quit()


def xml():
    f = open('compete.csv')
    df = pd.read_csv('compete.csv')
    xml_ = ('\n'.join(df.apply(convert_row, axis=1)))
    xml_ = str(("<webstore>", xml_, "</webstore>"))
    with open("compete.xml", "w") as f:
        f.write("<webstore>" + '\n'.join(df.apply(convert_row, axis=1)) + "</webstore>")


def convert_row(row):
    return """<competitor>
    <id>%s</id>
   <product>%s</product>
   <storename>%s</storename>
   <place>%s</place>
   <totalnum>%s</totalnum>
   <price>%s</price>
   <shipping>%s</shipping>
    <delivery>%s</delivery>
    <availability>%s</availability>
    
   </competitor>""" % (
        row.id, row[1], row.storename, row.place, row.totalnum, row.price, row.shipping, row.delivery,
        row.availability)


try:
    ReadXml()
    Scrap()
except Exception as e:
    print(e)

xml()
