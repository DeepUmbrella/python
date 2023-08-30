import os
import time
from py_mysql import SQL_CONNECTION
from write_to_file import FileDataSet

database = SQL_CONNECTION.get_sql_instance("pysql")

runner = database.cursor()


root_dir = os.path.join(os.path.dirname(__file__), "../../")

file_data: FileDataSet = FileDataSet(os.path.join(root_dir, "data.txt"))

query = "Insert into test_data values(%s, %s,%s, %s,%s, %s)"


per_commit_insert = 0

for item in file_data.read_all():

    runner.execute(query, (item['name'], item['id'], item['gold'],
                   item['level'], item['register_time'], item['last_login_time']))
    per_commit_insert += 1
    if (per_commit_insert >= 10):
        database.commit()
        per_commit_insert = 0
        print("committing ...........")
        time.sleep(1)


database.commit()


file_data.save_and_close()
SQL_CONNECTION.close_sql_instance()
