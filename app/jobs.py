import datetime as dt
import requests


def to_tlg(msg):
    url = f"https://api.telegram.org/bot279783998:AAE6cxVCwU97lSbyAu0Af6EWrhpAIUV6wno/sendMessage?chat_id=-155357321&text={msg}"
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
