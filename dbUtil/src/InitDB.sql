CREATE DATABASE IF NOT EXISTS demo4;
use demo4;

/* table format: <REGION>_<SYMBOL>_<DATA_TYPE>_<PERIOD>*/


CREATE TABLE IF NOT EXISTS tw_stock_price_minute (

  symbol_id INT NOT NULL,
  ts DATETIME NOT NULL,
  Open DECIMAL(10, 2),
  High DECIMAL(10, 2),
  Low  DECIMAL(10,2),
  Close DECIMAL(10,2),
  Volume BIGINT,
  PRIMARY KEY (symbol_id, ts)
  )
  PARTITION BY RANGE (YEAR(ts)) (
    PARTITION p2019 VALUES LESS THAN (2020),
    PARTITION p2020 VALUES LESS THAN (2021),
    PARTITION p2021 VALUES LESS THAN (2022),
    PARTITION p2022 VALUES LESS THAN (2023),
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025)

);

CREATE TABLE IF NOT EXISTS tw_future_price_minute (

  symbol_id CHAR(10) NOT NULL,
  ts DATETIME NOT NULL,
  Open DECIMAL(10, 2),
  High DECIMAL(10, 2),
  Low  DECIMAL(10,2),
  Close DECIMAL(10,2),
  Volume BIGINT,
  PRIMARY KEY (symbol_id, ts)
  )
  PARTITION BY RANGE (YEAR(ts)) (
    PARTITION p2019 VALUES LESS THAN (2020),
    PARTITION p2020 VALUES LESS THAN (2021),
    PARTITION p2021 VALUES LESS THAN (2022),
    PARTITION p2022 VALUES LESS THAN (2023),
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025)

);

/*CREATE INDEX idx_ts ON tw_stock_price_minute (ts);*/
/*ALTER TALBE tw_stock_price_minute ADD PARTITION (PARTITION p2025 VALUES LESS THAN (2026));*/

CREATE TABLE IF NOT EXISTS tw_stock_price_day (
  symbol_id INT NOT NULL,
  ts DATETIME NOT NULL,
  Open DECIMAL(10, 2),
  High DECIMAL(10, 2),
  Low  DECIMAL(10,2),
  Close DECIMAL(10,2),
  Volume BIGINT,
  PRIMARY KEY (symbol_id, ts),
  INDEX idx_ts (ts)
  )
 
  PARTITION BY RANGE (YEAR(ts)) (
    PARTITION p2000 VALUES LESS THAN (2001),
    PARTITION p2001 VALUES LESS THAN (2002),
    PARTITION p2002 VALUES LESS THAN (2003),
    PARTITION p2003 VALUES LESS THAN (2004),
    PARTITION p2004 VALUES LESS THAN (2005),
    PARTITION p2005 VALUES LESS THAN (2006),
    PARTITION p2006 VALUES LESS THAN (2007),
    PARTITION p2007 VALUES LESS THAN (2008),
    PARTITION p2008 VALUES LESS THAN (2009),
    PARTITION p2009 VALUES LESS THAN (2010),
    PARTITION p2010 VALUES LESS THAN (2011),
    PARTITION p2011 VALUES LESS THAN (2012),
    PARTITION p2012 VALUES LESS THAN (2013),
    PARTITION p2013 VALUES LESS THAN (2014),
    PARTITION p2014 VALUES LESS THAN (2015),
    PARTITION p2015 VALUES LESS THAN (2016),
    PARTITION p2016 VALUES LESS THAN (2017),
    PARTITION p2017 VALUES LESS THAN (2018),
    PARTITION p2018 VALUES LESS THAN (2019),
    PARTITION p2019 VALUES LESS THAN (2020),
    PARTITION p2020 VALUES LESS THAN (2021),
    PARTITION p2021 VALUES LESS THAN (2022),
    PARTITION p2022 VALUES LESS THAN (2023),
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025)
);

CREATE TABLE IF NOT EXISTS tw_stock_fundamental_month (

  symbol_id INT NOT NULL,
  fiscal_year INT NOT NULL,
  fiscal_quarter INT NOT NULL,
  revenue DECIMAL(15, 2),
  gross_profit DECIMAL(15, 2),
  net_profit DECIMAL(15, 2),
  PRIMARY KEY (symbol_id, fiscal_year, fiscal_quarter)

);

/*
CREATE TABLE tw_stock_fundamental_quarter {


}
*/


