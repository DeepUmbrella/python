from py_mysql import SQL_CONNECTION


sql_instance = SQL_CONNECTION.get_sql_instance()

runner = sql_instance.cursor()

runner.execute("SELECT * FROM `player` LIMIT 10 ")

results: tuple = runner.fetchall()

for player in results:

    print(player)

SQL_CONNECTION.close_sql_instance()
