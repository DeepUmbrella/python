﻿from generate_data_module import generate_data
from write_to_file import FileDataSet
from pyecharts.charts import Bar

import os


root_dir = os.path.join(os.path.dirname(__file__), "../../")

file_data: FileDataSet = FileDataSet(os.path.join(root_dir, "data.txt"))

data = generate_data(100)


for item in data:

    file_data.write_to_file(item.toJson())

res = []
for item in file_data.read_lines(1):
    print(item, type(item))
    res.append(item)

file_data.save_and_close()

result = res[0]
bar = Bar()
bar.add_xaxis(["id", "gold", "level"])
bar.add_yaxis("name", [result["id"], result["gold"], result["level"]])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()
