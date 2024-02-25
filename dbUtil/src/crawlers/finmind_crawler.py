from .crawler import Crawler
from FinMind.data import DataLoader
import os
from loguru import logger
import pandas as pd

class finmindCrawler(Crawler):

    def __init__(self):
        api = DataLoader()
        self.api = api
        logger.info(f"finmind api init!")

    def __del__(self):
        logger.info(f"finmind api logout!")


    def fetch_data_by_file(self, path, symbol_id):
        logger.debug(f"crawling symbol: {symbol_id} by finmind file...")
        if (os.path.getsize(path + symbol_id + ".csv") < 4096):
            logger.error(f"{path}+{symbol_id}.csv is empty!")
            return
        df = pd.read_csv(path + symbol_id + ".csv")
        df = df[["date", "open", "max", "min", "close", "Trading_Volume"]]
        df['date'] = pd.to_datetime(df["date"].str.split(' ', 1).str[0])
        df.rename(columns={'date': 'ts', 'open': 'Open', 'max': 'High', 'min': 'Low', 'close': 'Close', 'Trading_Volume': 'Volume'}, inplace=True)
        df["symbol_id"] = symbol_id
        df = df.drop_duplicates(subset='ts', keep='first')
        return df

    def fetch_data_by_api(self, symbol_id, start_date, end_date):
        logger.debug(f"crawling symbol: {symbol_id} by finmind api...")
        df = self.api.taiwan_stock_daily(
            stock_id=symbol_id,
            start_date=start_date,
            end_date=end_date
        )
        df = df[["date", "open", "max", "min", "close", "Trading_Volume"]]
        df['date'] = pd.to_datetime(df["date"].str.split(' ', 1).str[0])
        df.rename(columns={'date': 'ts', 'open': 'Open', 'max': 'High', 'min': 'Low', 'close': 'Close','Trading_Volume': 'Volume'}, inplace=True)
        df["symbol_id"] = symbol_id
        df = df.drop_duplicates(subset='ts', keep='first')

        return df