
import random
import datetime
import json
from typing import List


class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.id = player["id"]
        self.gold = player["gold"]
        self.level = player["level"]
        self.register_time = player["register_time"]
        self.last_login_time = player["last_login_time"]

    def __str__(self):

        out_json = {
            "name": self.name,
            "id": self.id,
            "gold": self.gold,
            "level": self.level,
            "register_time": self.register_time,
            "last_login_time": self.last_login_time
        }

        return json.dumps(out_json)

    def toJson(self):
        return self.__str__()


def generate_random_datetime(start_year, end_year):
    start_date = datetime.datetime(start_year, 1, 1)
    end_date = datetime.datetime(end_year, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return f"{random_date}"


def generate_data(num_rows) -> List[Player]:
    players = []
    for _ in range(num_rows):
        name = f"Player{random.randint(1, 100)}"
        id = random.randint(1000, 9999)
        gold = random.randint(0, 1000)
        level = random.randint(1, 100)
        register_time = generate_random_datetime(2010, 2023)
        last_login_time = generate_random_datetime(2020, 2023)
        player = Player({"name": name, "id": id, "gold": gold,
                        "level": level, "register_time": register_time, "last_login_time": last_login_time})
        players.append(player)
    return players


if (__name__ == "__main__"):
    # 生成10行数据
    data = generate_data(10)

    # 打印数据
    for player in data:
        print(player)
