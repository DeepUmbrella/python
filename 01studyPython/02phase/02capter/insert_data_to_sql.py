from py_mysql import SQL_CONNECTION
from datetime import datetime
sql = SQL_CONNECTION.get_sql_instance()

runner = sql.cursor()

sql_str = "INSERT INTO `player_vip` VALUES(%s ,%s, %s ,%s, %s ,%s)"

runner.execute(sql_str, (None, "John", str(23), datetime.now(),
               datetime.now(), "123456"))

sql.commit()
