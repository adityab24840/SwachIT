class DatabaseModel:
    def __init__(self, db_url):
        self.db_url = db_url
        self.connection = None

    def connect(self):
        import sqlite3
        self.connection = sqlite3.connect(self.db_url)

    def fetch_records(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        return records

    def close_connection(self):
        if self.connection:
            self.connection.close()