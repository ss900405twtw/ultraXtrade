# dbUtil

`dbUtil` is designed to facilitate interaction with a MySQL database for the purposes of updating market data and querying data for strategy development and backtesting in a Python environment.

## Features

- **Data Update**: Efficiently update market data to MySQL database.
- **Data Querying**: Retrieve historical data from the database for analysis and backtesting.


## Data Update

To update market data to a specific MySQL database and table, use the following command:
### Usage
```bash
python3 main.py -d <db_name> -t <table_name>
```




## Data Querying

The `dbUtil` module provides a `DatabaseManager` class that allows you to query data from your MySQL database. This can be particularly useful for strategy development and backtesting within a Python environment.

### Usage

To query data from the database, follow these steps:

1. **Initialize the DatabaseManager**: Create an instance of the `DatabaseManager` class by providing your MySQL connection settings.

    ```python
    from database import DatabaseManager

    # Replace 'my_sql_setting' with your actual MySQL connection settings
    my_sql_setting = {
        'host': 'your_host',
        'user': 'your_username',
        'password': 'your_password',
        'database': 'your_database'
    }

    db_manager = DatabaseManager(my_sql_setting)
    ```

2. **Query K-bar Data**: Use the `readKbars` method of the `DatabaseManager` instance to retrieve K-bar data for a specific stock symbol and date range.

    ```python
    # Call the readKbars method with the table name, stock symbol, start date, and end date
    df = db_manager.readKbarsFromDB(table_name, symbol_id, start_date, end_date)

    # Example:
    df = db_manager.readKbarsFromDB('tw_stock_price_day', '2454', '2019-06-25', '2019-07-10')
    ```

    The `readKbarsFromDB` method will return the queried data in a format of pandas DataFrame.


## Configuration

Ensure that you have the correct MySQL connection settings before attempting to query the database. The connection settings should be provided as a dictionary to the `DatabaseManager` when initializing it.

## Dependencies

Make sure all dependencies are installed. The `dbUtil` module may require libraries such as `pandas`, `sqlalchemy`, and `mysql-connector-python` or `pymysql`. You can install these using `pip`:

```bash
pip install pandas sqlalchemy mysql-connector-python