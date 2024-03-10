from crawlers import shioajiCrawler, yfinanceCrawler, finmindCrawler

def crawler_factory(table, **kwargs):
  if table in ["tw_stock_price_minute", "tw_future_price_minute"]:
      return shioajiCrawler(kwargs)
  elif table in ["tw_stock_price_day"]:
      return yfinanceCrawler()
      # return finmindCrawler()
  else:
      raise ValueError(f"Unknown table: {table} is used!")
