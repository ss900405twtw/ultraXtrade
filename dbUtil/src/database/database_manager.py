import sqlite3
import pymysql
import numpy as np
import time
import sys
import pandas as pd
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy import exc
import datetime
from utils import *

class DatabaseManager:
    def __init__(self, db_config):
        self.db_config = db_config
        self.db_name = db_config['db']
        self.engine = create_engine(f"mysql+pymysql://{self.db_config['user']}:{self.db_config['password']}@{self.db_config['host']}:{self.db_config['port']}/{self.db_name}")
        self.conn = pymysql.connect(**self.db_config)
        self.cursor = self.conn.cursor()
        logger.info(f"Current DB: {self.db_name} init!")

    def __del__(self):
        if self.conn:
            self.conn.close()
            logger.info(f"Current DB: {self.db_name} closed!")


    def checkTableExist(self, tablename):
        command = f"SHOW TABLES FROM {self.db_name} LIKE '{tablename}'"
        self.cursor.execute(command)
        ret = self.cursor.fetchall()

        return len(ret) > 0

    def checkIdxExist(self, tablename, symbol_id):
        command = f"SELECT 1 FROM {tablename} WHERE symbol_id = '{symbol_id}'"
        self.cursor.execute(command)
        ret = self.cursor.fetchall()

        return len(ret) > 0

    def checkLastTs(self, tablename, symbol_id):
        command = f"SELECT MAX(ts) AS last_date_time FROM {tablename} WHERE symbol_id = '{symbol_id}';"
        self.cursor.execute(command)
        time.sleep(0.5)
        ret = self.cursor.fetchall()
        return ret[0][0]

    def get_all_stock_id(self, table):
        command = f"SELECT DISTINCT symbol_id from {table};"
        self.cursor.execute(command)
        time.sleep(0.5)
        ret = self.cursor.fetchall()
        return ret


    def backFillKbars(self, symbol_ids, table, crawler):
        today = get_today()
        today = add_N_Days(date=today, days=-1)
        if not self.checkTableExist(table):
            logger.error(f"table: {table} not exists, please check!")
            return

        logger.info(f"backFilling {len(symbol_ids)} symbols to table: {table}")
        cnt = 0
        for symbol_id in symbol_ids:
            cnt += 1
            lastdatetime = self.checkLastTs(table, symbol_id)
            if (self.checkIdxExist(table, symbol_id)):

                start = add_N_Days(date=lastdatetime.date(), days=1)
                end = today
                if (start < end):
                    logger.info(f"update exists symbol: {symbol_id} from {start} to {end} to table: {table}, {cnt}/{len(symbol_ids)}...")
                else:
                    logger.info(f"symbol: {symbol_id} is already up to date: from: {start} to {end}, {cnt}/{len(symbol_ids)} ...")
                    continue
            else:
                start = '2010-01-01'
                end = today
                logger.warning(f"update new symbol: {symbol_id} to table: {table}, {cnt}/{len(symbol_ids)}")

            df = crawler.fetch_data_by_api(symbol_id, str(start), str(end))
            if len(df) == 0:
                logger.error(f"symbol: {symbol_id} is empty, please check!, {cnt}/{len(symbol_ids)}")
                continue
            time.sleep(5)
            try:
                df.to_sql(name=table, con=self.engine, if_exists='append', index=False)
            except exc.IntegrityError:
                logger.warning(f"Duplicate entry error of: {symbol_id}")
                continue


    def readKbarsFromDB(self, tablename, symbol_id, start='2021-07-01', end='2021-07-05'):

        query = f"SELECT * FROM {tablename} WHERE symbol_id = '{symbol_id}' AND ts BETWEEN '{start}' AND '{end}';"
        df = pd.read_sql_query(query, self.engine)

        return df





