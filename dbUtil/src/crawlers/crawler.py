class Crawler:
    # fetch data by file and convert to mySQL format
    def fetch_data_by_file(self, path, symbol_id):
        raise NotImplementedError("child class need to implement fetch_data_by_file")

    # fetch data by api and convert to mySQL format
    def fetch_data_by_api(self, symbol_id, start_date, end_date):
        raise NotImplementedError("child class need to implement fetch_data_by_api")