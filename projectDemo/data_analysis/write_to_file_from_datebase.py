import datetime
import json
import os
import time
from py_mysql import SQL_CONNECTION
from write_to_file import FileDataSet


class TestDataRecord:
    def __init__(self, testDataKeys: tuple = tuple()):
        self.keys = testDataKeys

    def transformJson(self, data: list | tuple) -> str:
        origin = dict()
        for key in self.keys:

            value = data[self.keys.index(key)]
            if isinstance(value, datetime.datetime):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            origin[key] = value
        return json.dumps(origin)


database = SQL_CONNECTION.get_sql_instance("pysql")

runner = database.cursor()


root_dir = os.path.join(os.path.dirname(__file__), "../../")

file_data: FileDataSet = FileDataSet(
    os.path.join(root_dir, "data_from_database.txt"))

key_tuple = ("name", "id", "gold", "level", "register_time", "last_login_time")

record = TestDataRecord(key_tuple)

query = f"select {','.join(key_tuple)} from test_data"


runner.execute(query)

results: tuple = runner.fetchall()

per_commit_insert = 0

for item in results:
    file_data.write_to_file(record.transformJson(item))
    per_commit_insert += 1
    if (per_commit_insert >= 10):
        file_data.save_to_file()
        per_commit_insert = 0
        print("committing ...........")
        time.sleep(1)


database.commit()
file_data.save_and_close()
SQL_CONNECTION.close_sql_instance()
