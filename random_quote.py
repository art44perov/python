import googletrans
import requests
import json
from googletrans import Translator
import logging
from _datetime import datetime

logging.basicConfig(level=logging.INFO, filename="Quotes_log.log",filemode="a")

def Quotes():

    translator = Translator()
    str_query = "https://favqs.com/api/qotd"
    response = requests.get(str_query)
    if response.status_code == 200:
        stroke_s = json.loads(response.text)['quote']['body']
        res = translator.translate(stroke_s, src='en', dest='ru')
        logging.info(f'{datetime.now()}     quotes day: {res.text}')
        return res.text
    else:
        logging.error('NO connection...')
        return "No connection..."


print(Quotes())
