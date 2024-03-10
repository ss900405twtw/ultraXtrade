import datetime
import requests
import pandas as pd
def get_today():
    return datetime.date.today()

def sub_N_Days(
        days#=1
        ,date=datetime.date.today()
        ):
    return date - datetime.timedelta(days)

def add_N_Days(
        days#=1
        ,date=datetime.date.today()
        ):
    return date + datetime.timedelta(days)


def get_al_listed_stocks():
    url = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
    res = requests.get(url)
    df = pd.read_html(res.text)[0]
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    df = df.dropna(thresh=3, axis=0).dropna(thresh=3, axis=1)
    df = df[df['CFICode'] == 'ESVUFR']
    stocks = list(df['有價證券代號及名稱'])
    stocks_02 = set([item[:4] for item in stocks])
    return stocks_02

def get_all_otc_stocks():
    url = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=4"
    res = requests.get(url)
    df = pd.read_html(res.text)[0]
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    df = df.dropna(thresh=3, axis=0).dropna(thresh=3, axis=1)
    df = df[df['CFICode'] == 'ESVUFR']
    stocks = list(df['有價證券代號及名稱'])
    stocks_04 = set([item[:4] for item in stocks])
    return stocks_04