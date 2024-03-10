import json
import sys
import os
import numpy as np
from loguru import logger
from pathlib import Path
import argparse
from factory import crawler_factory
from database import DatabaseManager
from utils import get_al_listed_stocks, get_all_otc_stocks

logger.remove()
logger.add(sys.stdout, level="DEBUG")
logger.add('tmp.log', level="DEBUG")


def db_update_main():
    parser = argparse.ArgumentParser(description="argparse for db update")
    parser.add_argument("-d", "--database", help="provide db name you want to operate", dest="db", type=str, required=True)
    parser.add_argument("-t", "--table", help="provide table name you want to update", dest="table", type=str,required=True,
                        choices=["tw_stock_price_minute", "tw_stock_price_day", "tw_future_price_minute", "tw_stock_fundamental_month"])



    my_sql_login_file = "./login/mysql_login.json"
    shioaji_login_file = "./login/shioaji_login.json" # optional if you want to crawl day price


    args = parser.parse_args()
    logger.info(f"database: {args.db}, table: {args.table}")

    with open(my_sql_login_file) as json_file:
        mysql_db_settings = json.load(json_file)
    db_manager = DatabaseManager(mysql_db_settings)


    login_kws = {}
    if os.path.exists(shioaji_login_file):
        p = Path(shioaji_login_file)
        login_kws = json.loads(p.read_text())


    crawler = crawler_factory(args.table, **login_kws)
    listed_stocks = get_al_listed_stocks()
    otc_stocks = get_all_otc_stocks()
    all_symbols = listed_stocks | otc_stocks
    db_manager.backFillKbars(all_symbols, args.table, crawler)


if __name__ == "__main__":
    db_update_main()
