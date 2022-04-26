# Micro Crawler Installaton Guide
## _The Last Markdown Editor, Ever_

![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

## Requirments

- Python3 version >= 3.7
- pip3 version >=21.0.0
- requirements.txt 
> Note:Python version must be 3.7 or greater otherwise libraries will not be caompatible with lower verion
`python3 --version` for python version check
`pip3 --version` for pip version check

## Installation

MC requires [Python](https://www.python.org/downloads/release/python-3713/) v3.7+ to run.

Clone the repo and intall the depnedencies
```sh
git clone https://user@bitbucket.org/rapidevosinteam/micro_crawler.git
cd micro_cralwer
```

### install Celery

```sh
sudo apt update
sudo apt install python-celery
```
### upgrade cryptography using following command
```sh
pip install cryptography --upgrade
```

### install dependencies

```sh
pip install -r requriements.txt
```

## Update in config file

Configuration update is require to run the server properly.
Follwoing updates are required in `config/config.json`

| Config | Update |
| ------ | ------ |
| Host | `update with your ip or with the ip of running micro_crawler ip`  |
| celery | `celery ip attached to that running microcrawler server` |

## update the kafka brokers IP in version 4.0
update the kafka brokers IP for version 4.0
> update the `Host` `PORT` `BROKER_IPS` in `micro_crawler/setting.py`

## `app.py` configuration
> In `micro_crawler/app.py` check the Last Line
```sh
    #app.run(debug=True)
    socketio.run(app, host=HOST, port=PORT, debug=DEBUG)
```
`socketio.run` should be un-comment and `app.run` should be commented

## Start the Server
This will start the server
```sh
cd micro_crawler
./run.sh
```
###  Note some dependencies are not included in requirements.txt so need to install these libraries using pip

