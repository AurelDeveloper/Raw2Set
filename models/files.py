import json
import sqlite3
from typing import List

class DataModel:
    def __init__(self, db_file: str):
        self.db_file = db_file
        self._initialize_database()

    def _initialize_database(self):
        with sqlite3.connect(self.db_file) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS json_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    backup JSON NOT NULL
                )
            ''')

    def process_and_store_data(self, data: List[str], json_backup_file: str):
        json_data = json.dumps(data)
        with open(json_backup_file, 'w') as file:
            file.write(json_data)
        with sqlite3.connect(self.db_file) as conn:
            conn.execute('INSERT INTO json_data (backup) VALUES (?)', (json_data,))