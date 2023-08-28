
import random
import datetime
import json

class Player:
    def __init__(self, name, id, gold, level, register_time, last_login_time):
        self.name = name
        self.id = id
        self.gold = gold
        self.level = level
        self.register_time = register_time
        self.last_login_time = last_login_time

    def __str__(self):
        return f'\{name: {self.name}, ID: {self.id}, Gold: {self.gold}, Level: {self.level}, Register Time: {self.register_time}, Last Login Time: {self.last_login_time}\}'

def generate_random_datetime(start_year, end_year):
    start_date = datetime.datetime(start_year, 1, 1)
    end_date = datetime.datetime(end_year, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def generate_data(num_rows):
    players = []
    for _ in range(num_rows):
        name = f"Player{random.randint(1, 100)}"
        id = random.randint(1000, 9999)
        gold = random.randint(0, 1000)
        level = random.randint(1, 100)
        register_time = generate_random_datetime(2010, 2023)
        last_login_time = generate_random_datetime(2020, 2023)
        player = Player(name, id, gold, level, register_time, last_login_time)
        players.append(player)
    return players

# 生成10行数据
data = generate_data(10)

# 打印数据
for player in data:
    print(player)