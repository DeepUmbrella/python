from dotenv import load_dotenv
from pymysql import Connection
from time import sleep, time
import os


c_abs_path = os.path.dirname(__file__)
t_abs_path = os.path.join(c_abs_path, "../../../.env")
load_dotenv(dotenv_path=t_abs_path)


class SQL_CONNECTION:
    try_count = 0
    sql_instance = None

    def __get_sql_instance(self, message: str = f"Start Connection .... {time()}") -> (Connection | None):
        if SQL_CONNECTION.sql_instance != None:
            print("Already connected to sql")

            return SQL_CONNECTION.sql_instance

        if (SQL_CONNECTION.try_count > 3):
            print("Failed to connect to sql after 3 attempts")
            print("Please check your .env file or your network connection")
            return None

        try:
            if not message:
                pass
            else:
                print(f"{message}")
            host = os.environ.get("MYSQL_HOST")
            port = int(os.environ.get("MYSQL_PORT"))
            user = os.environ.get("MYSQL_USER")
            password = os.environ.get("MYSQL_PASSWORD")
            database = os.environ.get("MYSQL_DATABASE")
            sql_instance = Connection(host=host, port=port,
                                      database=database,
                                      user=user, password=password)
            print(f"Connection to {host} sql successful! {time()}")
            return sql_instance
        except:
            SQL_CONNECTION.try_count += 1

            print(f"Connection to {host} sql failed!")

            return self.__get_sql_instance(f"Retrying {SQL_CONNECTION.try_count} ...... {time()}")

    def __init__(self):
        SQL_CONNECTION.sql_instance = self.__get_sql_instance()

    def get_sql_instance(self):
        return SQL_CONNECTION.sql_instance

    def close_sql_instance(self):
        SQL_CONNECTION.sql_instance.close()
        SQL_CONNECTION.sql_instance = None


SQL_CONNECTION()
SQL_CONNECTION()
