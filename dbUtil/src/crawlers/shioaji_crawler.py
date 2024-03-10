from .crawler import Crawler
import json
import shioaji as sj
from pathlib import Path
import time
from loguru import logger
import pandas as pd

class shioajiCrawler(Crawler):

    def __init__(self, login_kws):
        api = sj.Shioaji(simulation=True)
        api.login(**login_kws, contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done."))
        time.sleep(5)
        self.api = api
        logger.info(f"Shioaji api init!")

    def __del__(self):
        self.api.logout()
        logger.info(f"Shioaji api logout!")


    def fetch_data_by_file(self, path, symbol_id):
        logger.debug(f"crawling symbol: {symbol_id} by shioaji file...")
        df = pd.read_csv(path + symbol_id + ".csv")
        df = df[["ts", "Open", "High", "Low", "Close", "Volume"]]
        df["symbol_id"] = symbol_id
        df = df.drop_duplicates(subset='ts', keep='first')
        return df

    def fetch_data_by_api(self, symbol_id, start_date, end_date):
        logger.debug(f"crawling symbol: {symbol_id} by shioaji api...")
        if (symbol_id.isdigit()):
            # stock
            contract = self.api.Contracts.Stocks[symbol_id]
        else:
            # future
            contract = self.api.Contracts.Futures[symbol_id][symbol_id + "R1"]

        kbars = self.api.kbars(contract, start=start_date, end=end_date)
        df = pd.DataFrame({**kbars})
        if (len(df)) == 0:
            return df
        df.ts = pd.to_datetime(df.ts)
        df.drop('Amount', axis=1, inplace=True)
        df["symbol_id"] = symbol_id
        df = df.drop_duplicates(subset='ts', keep='first')

        return df