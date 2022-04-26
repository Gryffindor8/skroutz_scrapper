# import requests
#
# cookies = {
#     'retat': '58.65.137.182x1650805238-0000640757f56cf4c659193953bbf357342524d3',
#     'policy_level': '%7B%22essential%22%3A%22true%22%2C%22performance%22%3A%22true%22%2C%22preference%22%3A%22true%22%2C%22targeting%22%3A%22true%22%7D',
#     'analytics_session': 'c0f6ba6c-6c0a-4fec-ad7c-6d4056e741fa',
#     '_sa_meta': '%7B%22app_type%22%3A%22web%22%2C%22cp%22%3A%22f%22%2C%22tags%22%3A%22%22%7D',
#     '__skr_nltcs_ss': '%7B%22version%22%3A1%2C%22session%22%3A%22c0f6ba6c-6c0a-4fec-ad7c-6d4056e741fa%22%7D',
#     '_helmet_couch': 'pfHK0KWHDd61AVaNbGlzW7OPtODX%2F%2BG0ZAol5kW5nmUsVQ81aoniRrcXm%2Flo0Et1X7x7bEhNYGupxPc20K9XBKbF2lZsEhjoZ5Y07K0njI1rrd9pNEePEIehyyUzWZY5dHzWDnGV3hGdmFFvQA1VhitadPugrEdj9LI3J3bUfYRaCf2VcScdeuYTx6N%2FzNxeXvAus7I7VuMzAzCUcnIvfFotVlAf5LHk6KbzNxVHT8pYY%2B2Sc8y9st1cs8alnibh7OBTQdSx5umyoG5%2B3Pbtj2yYPgiPbW5mw8HquFjZ6uCxaH5DVzx9zhUgk6PYLa1FD9lXLgAWQ9MO5WGUiGpj1AvFcJXve3qkbadhw7V%2FypK3Fi6z1%2FcYdlU31L3pgLlAPXhaY7GFxVgfrlrsGboRfMF3jtecc4wS7VZ%2BL4yKzpys9HLKSRet2hKJXUPjoOPg%2BmwB%2BqfHcs7f2%2F4XPzHryVPcSTGm84J2ONZNyTq5CZBwn1LKO2TFFiZ2UjmiAnfLTeZ5jEEN3UXOtRwXd87rsLgDfdUSjMzpVsWKAAWxtnsPdFkgQFUyDBpdzFrY0LlpkfAJxD6bIPVq0igSC6OscflI5f%2BoSN3EaWG3kZ3KPVyU74EZK81aCaLm%2BqLf0T23hQ%3D%3D--ZhXmCXvtm6dqAfm5--92jQkGcHYv%2BkrxPwqIDBLQ%3D%3D',
# }
#
# headers = {
#     'authority': 'www.skroutz.gr',
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#     # Already added when you pass json=
#     # 'content-type': 'application/json',
#     # Requests sorts cookies= alphabetically
#     # 'cookie': 'retat=58.65.137.182x1650805238-0000640757f56cf4c659193953bbf357342524d3; policy_level=%7B%22essential%22%3A%22true%22%2C%22performance%22%3A%22true%22%2C%22preference%22%3A%22true%22%2C%22targeting%22%3A%22true%22%7D; analytics_session=c0f6ba6c-6c0a-4fec-ad7c-6d4056e741fa; _sa_meta=%7B%22app_type%22%3A%22web%22%2C%22cp%22%3A%22f%22%2C%22tags%22%3A%22%22%7D; __skr_nltcs_ss=%7B%22version%22%3A1%2C%22session%22%3A%22c0f6ba6c-6c0a-4fec-ad7c-6d4056e741fa%22%7D; _helmet_couch=pfHK0KWHDd61AVaNbGlzW7OPtODX%2F%2BG0ZAol5kW5nmUsVQ81aoniRrcXm%2Flo0Et1X7x7bEhNYGupxPc20K9XBKbF2lZsEhjoZ5Y07K0njI1rrd9pNEePEIehyyUzWZY5dHzWDnGV3hGdmFFvQA1VhitadPugrEdj9LI3J3bUfYRaCf2VcScdeuYTx6N%2FzNxeXvAus7I7VuMzAzCUcnIvfFotVlAf5LHk6KbzNxVHT8pYY%2B2Sc8y9st1cs8alnibh7OBTQdSx5umyoG5%2B3Pbtj2yYPgiPbW5mw8HquFjZ6uCxaH5DVzx9zhUgk6PYLa1FD9lXLgAWQ9MO5WGUiGpj1AvFcJXve3qkbadhw7V%2FypK3Fi6z1%2FcYdlU31L3pgLlAPXhaY7GFxVgfrlrsGboRfMF3jtecc4wS7VZ%2BL4yKzpys9HLKSRet2hKJXUPjoOPg%2BmwB%2BqfHcs7f2%2F4XPzHryVPcSTGm84J2ONZNyTq5CZBwn1LKO2TFFiZ2UjmiAnfLTeZ5jEEN3UXOtRwXd87rsLgDfdUSjMzpVsWKAAWxtnsPdFkgQFUyDBpdzFrY0LlpkfAJxD6bIPVq0igSC6OscflI5f%2BoSN3EaWG3kZ3KPVyU74EZK81aCaLm%2BqLf0T23hQ%3D%3D--ZhXmCXvtm6dqAfm5--92jQkGcHYv%2BkrxPwqIDBLQ%3D%3D',
#     'origin': 'https://www.skroutz.gr',
#     'referer': 'https://www.skroutz.gr/s/24573214/Newplan-%CE%A7%CE%B1%CE%BB%CE%AF-%CE%94%CE%B9%CE%AC%CE%B4%CF%81%CE%BF%CE%BC%CE%BF%CF%82-33290-957-Toronto-80x150%CE%B5%CE%BA.html',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Linux"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
#     'x-csrf-token': 'kRMJSGk5XxjG6iy3DtVMUCVljzIUy0rw0GcUCm7tEh8qAAIBpgbj5lrQPfsCWtxIld0iBMOPIjVCO+ZZC/MKgA==',
#     'x-requested-with': 'XMLHttpRequest',
# }
#
# json_data = {
#     'product_ids': [
#         62947194,
#         104548789,
#         99179051,
#         104220626,
#         91059498,
#         83417598,
#         86372902,
#         99162915,
#         101463159,
#         62960979,
#         62829775,
#         99196579,
#         99031519,
#         99083386,
#         99226557,
#         89726148,
#         99012348,
#         99085745,
#         99101689,
#         99161982,
#         61851386,
#         111928957,
#         110899397,
#         112010108,
#         99271101,
#         108652779,
#         92930260,
#         61919201,
#         91630817,
#         91899991,
#         63808133,
#         110180779,
#     ],
# }
#
# response = requests.post('https://www.skroutz.gr/personalization/product_prices.json', cookies=cookies, headers=headers, json=json_data)
# print(response.json())

import requests

import requests

cookies = {
    'retat': '58.65.137.182x1650805238-0000640757f56cf4c659193953bbf357342524d3',
    'policy_level': '%7B%22essential%22%3A%22true%22%2C%22performance%22%3A%22true%22%2C%22preference%22%3A%22true%22'
                    '%2C%22targeting%22%3A%22true%22%7D',
    'analytics_session': 'c0f6ba6c-6c0a-4fec-ad7c-6d4056e741fa',
    '_sa_meta': '%7B%22app_type%22%3A%22web%22%2C%22cp%22%3A%22f%22%2C%22tags%22%3A%22%22%7D',
    '__skr_nltcs_ss': '%7B%22version%22%3A1%2C%22session%22%3A%22c0f6ba6c-6c0a-4fec-ad7c-6d4056e741fa%22%7D',
    '_helmet_couch': 'jupO725kaI27OYbMrvk9o54cRpmFyXGqZVBo89WErn9hfvA7K'
                     '%2BvrI5aBfEpzonaNwvfqw388ZdjaLbqPckN0njWJ86InIXLAQQd7AX0rNXAHWt%2F7FAXc9MUiV4IoyqVG05vv9XFp'
                     '%2B4JOu3%2FbMFykgw6vUU2cMmJbimTqS%2FWpygwpEVZrB3SKlk1xG%2FYUhpjgV1ZG4ZQTplKPUFyaika9HPVo8Vhf9nX'
                     '%2B103zAr4uzgCda%2BM9dEGk7I%2BCyJT9KfkfUsbjP4zCiUjrPqHMPALFLeKaxgFeUF2ahV'
                     '%2FDg7jASYCE4Vi8oveW8bC7qDbaF6xLMQEKV5FNDNPTE4B3EJfoph14nSUjsoMEaL0SncdRaIlwbfxwBrfBj5K68eT3IjqFfqsilhmhy9%2FIxfAPb0gL8EwmDQ076XEPX6Jd%2B6In4w6nzv7o7y6Ep33YD7urdW05HYkdFTFBX%2FlChjWAqBRQg04ntW0KO9vrF7myAPjeN%2BYk8WZ7u6UQHlU0rmD96OD2tdAulrIngAMNrFuG8dgdGrVaAbJ2NKuWJW%2B2WoXT3LqkvWbatYPVUh5BfneeJrdE3xB5Ede8D0VpkYYG8oUEr9FEMI0%2FWQ4pAfM%2B%2B74NZQ2yruEBYsw6D9wNTYxTzj%2FNfQ%3D%3D--SbnBPwUH8YCb7e1P--giC2Ftc6%2FIojYMkPuRa%2BOw%3D%3D',
    'data_sli': '0',
    'data_imp': '%5B24573214%5D',
    'data_follow_skus': '%7B%22keyphrase%22%3A%22NewPlan%20-%20%CE%A7%CE%B1%CE%BB%CE%AF%20TORONTO%2033290%2F957%20-%20080X150%22%2C%22slo%22%3A%22popularity%22%7D',
    'data_follow_products': '%7B%22keyphrase%22%3A%22NewPlan%20-%20%CE%A7%CE%B1%CE%BB%CE%AF%20TORONTO%2033290%2F957'
                            '%20-%20080X150%22%2C%22slo%22%3A%22popularity%22%7D',
    'data_follow_categories': '%7B%22catspan_preferences%22%3Anull%7D',
    'data_follow_ecommerce_cart': '%7B%22slo%22%3A%22popularity%22%7D',
}

headers = {
    'authority': 'www.skroutz.gr',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'retat=58.65.137.182x1650805238-0000640757f56cf4c659193953bbf357342524d3; policy_level=%7B%22essential%22%3A%22true%22%2C%22performance%22%3A%22true%22%2C%22preference%22%3A%22true%22%2C%22targeting%22%3A%22true%22%7D; analytics_session=c0f6ba6c-6c0a-4fec-ad7c-6d4056e741fa; _sa_meta=%7B%22app_type%22%3A%22web%22%2C%22cp%22%3A%22f%22%2C%22tags%22%3A%22%22%7D; __skr_nltcs_ss=%7B%22version%22%3A1%2C%22session%22%3A%22c0f6ba6c-6c0a-4fec-ad7c-6d4056e741fa%22%7D; _helmet_couch=jupO725kaI27OYbMrvk9o54cRpmFyXGqZVBo89WErn9hfvA7K%2BvrI5aBfEpzonaNwvfqw388ZdjaLbqPckN0njWJ86InIXLAQQd7AX0rNXAHWt%2F7FAXc9MUiV4IoyqVG05vv9XFp%2B4JOu3%2FbMFykgw6vUU2cMmJbimTqS%2FWpygwpEVZrB3SKlk1xG%2FYUhpjgV1ZG4ZQTplKPUFyaika9HPVo8Vhf9nX%2B103zAr4uzgCda%2BM9dEGk7I%2BCyJT9KfkfUsbjP4zCiUjrPqHMPALFLeKaxgFeUF2ahV%2FDg7jASYCE4Vi8oveW8bC7qDbaF6xLMQEKV5FNDNPTE4B3EJfoph14nSUjsoMEaL0SncdRaIlwbfxwBrfBj5K68eT3IjqFfqsilhmhy9%2FIxfAPb0gL8EwmDQ076XEPX6Jd%2B6In4w6nzv7o7y6Ep33YD7urdW05HYkdFTFBX%2FlChjWAqBRQg04ntW0KO9vrF7myAPjeN%2BYk8WZ7u6UQHlU0rmD96OD2tdAulrIngAMNrFuG8dgdGrVaAbJ2NKuWJW%2B2WoXT3LqkvWbatYPVUh5BfneeJrdE3xB5Ede8D0VpkYYG8oUEr9FEMI0%2FWQ4pAfM%2B%2B74NZQ2yruEBYsw6D9wNTYxTzj%2FNfQ%3D%3D--SbnBPwUH8YCb7e1P--giC2Ftc6%2FIojYMkPuRa%2BOw%3D%3D; data_sli=0; data_imp=%5B24573214%5D; data_follow_skus=%7B%22keyphrase%22%3A%22NewPlan%20-%20%CE%A7%CE%B1%CE%BB%CE%AF%20TORONTO%2033290%2F957%20-%20080X150%22%2C%22slo%22%3A%22popularity%22%7D; data_follow_products=%7B%22keyphrase%22%3A%22NewPlan%20-%20%CE%A7%CE%B1%CE%BB%CE%AF%20TORONTO%2033290%2F957%20-%20080X150%22%2C%22slo%22%3A%22popularity%22%7D; data_follow_categories=%7B%22catspan_preferences%22%3Anull%7D; data_follow_ecommerce_cart=%7B%22slo%22%3A%22popularity%22%7D',
    'referer': 'https://www.skroutz.gr/c/1765/Xalia-Saloniou/m/34352/Newplan.html?keyphrase=TORONTO+33290%2F957+080X150&o=NewPlan+-+%CE%A7%CE%B1%CE%BB%CE%AF+TORONTO+33290%2F957+-+080X150',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 '
                  'Safari/537.36',
}

response = requests.get('https://www.skroutz.gr/s/24573214/Newplan-%CE%A7%CE%B1%CE%BB%CE%AF-%CE%94%CE%B9%CE%AC%CE%B4'
                        '%CF%81%CE%BF%CE%BC%CE%BF%CF%82-33290-957-Toronto-80x150%CE%B5%CE%BA.html', cookies=cookies,
                        headers=headers)
print(response.content)