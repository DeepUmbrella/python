
import json
import os
import numpy
import matplotlib.pyplot as plt
from time import sleep
import datetime


from neural_network import Neural_Network


c_abs_path = os.path.dirname(__file__)

train_file_path = os.path.join(c_abs_path, "data/train/train_100.csv")
train_file_path2 = os.path.join(c_abs_path, "data/train/mnist_train.csv")
test_file_path = os.path.join(c_abs_path, "data/test/test_10.csv")
test_file_path2 = os.path.join(c_abs_path, "data/test/mnist_test.csv")

print(train_file_path)
print(test_file_path)


with open(train_file_path2, 'r') as data_file:
    train_data_list = data_file.readlines()
with open(test_file_path2, 'r') as test_data_file:
    test_data_list = test_data_file.readlines()[1:9999:99]

input_nodes = 784
hidden_nodes = 100
output_nodes = 10
learning_rate = 0.3

n_t = Neural_Network(input_nodes, hidden_nodes, output_nodes, learning_rate)

print(len(test_data_list))
mistake_rate = 1
if __name__ == "__main__":
    train_count = 0
    already_train_count = 0
    while mistake_rate > 0.01 and train_count < 10:
        mistake_count = 0
        for item in train_data_list:
            origin_data_arr = item.split(",")
            data_label = int(origin_data_arr[0])
            data_image = numpy.asfarray(origin_data_arr[1:])

            scaled_input = data_image/255.0 * 0.99 + 0.01

            targets = numpy.zeros(output_nodes) + 0.01

            targets[data_label] = 0.99

            finally_out = n_t.train(scaled_input, targets)
            already_train_count += 1
            if (already_train_count % 1000 == 0):
                print(
                    f"already train count to {already_train_count} ===========================>")

        train_count += 1
        print(
            f"train over {train_count} start test ===========================>")

        for item in test_data_list:
            origin_data_arr = item.split(",")
            data_label = int(origin_data_arr[0])
            data_image = numpy.asfarray(origin_data_arr[1:])

            scaled_input = data_image/255.0 * 0.99 + 0.01

            finally_out = n_t.query(scaled_input)
            if (data_label != finally_out):
                mistake_count += 1
            print(data_label, finally_out)
            # print(transform_data[0])

        mistake_rate = mistake_count / len(test_data_list)

        if (mistake_rate > 0.1):
            print(
                f"train over {train_count} mistake_rate:{mistake_rate}  ===========================>")

    print(
        f"train over ===========================> all train {train_count} 次  write WI to file")
    print(
        f"train over {train_count} mistake_rate:{mistake_rate}  ===========================>")

    with open(os.path.join(c_abs_path, f"data/train/WI{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.json"), 'w') as wih_file:
        wih_file.write(json.dumps({
            "WIH": n_t.wih.tolist(),
            "WHO": n_t.who.tolist(),
        }))
