
import os
import datetime as dt
import requests
from dotenv import load_dotenv

load_dotenv()

TLG_URL = os.getenv('TLG_URL')


def to_tlg(msg):
    url = f"{TLG_URL}={msg}"
    try:
        res = requests.get(url)
        return res.status_code
    except Exception as e:
        return str(e)


def do_something(path):
    with open(path, 'a') as f:
        f.write(f"from flask-crontab at {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} with love ❤️\n")


def do_once():
    to_tlg(f"from flask-crontab at {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} with love ❤️")
