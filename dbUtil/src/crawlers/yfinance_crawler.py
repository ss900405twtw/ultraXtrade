from .crawler import Crawler
import yfinance as yf
from loguru import logger
import pandas as pd

class yfinanceCrawler(Crawler):

    def __init__(self):
        logger.info(f"yfinance api init!")

    def __del__(self):
        logger.info(f"yfinance api logout!")


    def fetch_data_by_file(self, path, symbol_id):
        logger.debug(f"crawling symbol: {symbol_id} by yfinance file...")
        df = pd.read_csv(path + symbol_id + ".csv")
        df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]
        df['Date'] = pd.to_datetime(df["Date"].str.split(' ', 1).str[0])
        df.rename(columns={'Date': 'ts'}, inplace=True)
        df["symbol_id"] = symbol_id
        df = df.drop_duplicates(subset='ts', keep='first')
        return df

    def fetch_data_by_api(self, symbol_id, start_date, end_date):
        def get_stock():
            df = yf.download(symbol_id + ".TW", start=start_date, end=end_date)
            df = yf.download(symbol_id + ".TWO", start=start_date, end=end_date) if len(df) == 0 else df
            return df

        logger.debug(f"crawling symbol: {symbol_id} by yfinance api...")
        df = get_stock()
        # df["Date"] = df.index
        df.reset_index(inplace=True)
        df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]
        df = df.rename(columns={'Date': 'ts'})
        df["symbol_id"] = symbol_id
        df = df.drop_duplicates(subset='ts', keep='first')


        return df