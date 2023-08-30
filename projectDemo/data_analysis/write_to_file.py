

import json
import os
import time
from typing import List, TextIO, Union


class FileDataSet:

    def __init__(self, file_path: str):
        file_IO, create_ways = self.__open_file(file_path)
        self.__file: Union[TextIO, None] = file_IO
        self.create_ways = create_ways
        self.__file_seek = 0

        print(f"create_ways is {create_ways}")

    def __open_file(self, file_path: str) -> Union[TextIO, None]:
        try:
            if os.path.isdir(file_path):
                file_path = os.path.join(file_path, 'data.txt')
                # create new file base on current path
                if not os.path.exists(file_path):
                    return open(file_path, 'w', encoding="utf-8"), "isDir Exists"
                else:
                    return open(file_path, "+a", encoding="utf-8"), "isDir noExists"
            else:
                return open(file_path, '+a', encoding="utf-8"), "noIsDir append"
        except:
            return open("data.txt", "w", encoding="utf-8"), "Error to add"

    def write_to_file(self, data: str):
        # write data to file
        self.__file.write(data)
        self.__file.write('\n')

    def save_to_file(self):
        self.__file.flush()

    def save_and_close(self):
        self.__file.close()

    def read_lines(self, rows: int = 1) -> List[dict]:

        self.__file.seek(self.__file_seek)
        data_list = list()

        i = 0
        while i < rows:
            online_data = self.__file.readline().replace('\n', '')
            if not online_data:
                break
            data_list.append(json.loads(online_data))
            i += 1
        self.__file_seek = self.__file.tell()

        return data_list

    def read_all(self):
        self.__file.seek(0)
        data_list = list()
        for line in self.__file.readlines():
            data_list.append(json.loads(line.replace('\n', '')))
        return data_list

    def write_to_file(self, data: str):
        # write data to file
        self.__file.write(data)
        self.__file.write('\n')
        self.save_to_file()


if (__name__ == "__main__"):
    file_data: FileDataSet = FileDataSet(
        "D:\\project\\pythonProject\\studyPython\\data.txt")
    run = True
    while run:
        lines = file_data.read_lines(10)
        for line in lines:
            print(line)
        # sleep 1s
        if not lines:
            run = False
            break

        time.sleep(1)

    file_data.save_and_close()
