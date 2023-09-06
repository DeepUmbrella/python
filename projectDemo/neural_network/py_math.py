import numpy

if __name__ == "__main__":

    # 定义二维数组
    arr = numpy.array([[-4.49401501, 4.00950034, -1.81814867, 7.29718677],
                       [0.39924804, 4.68456316, 4.99394529, 4.84057254]])

    # 计算平均值
    mean = numpy.mean(arr)

    x = (arr - mean) ** 2

    print(x, "xxxxxxxxxxxxxx")
    # 计算平方差
    variance = numpy.mean((arr - mean) ** 2)

    # 计算标准差
    standard_deviation = numpy.sqrt(variance)

    print("平均值:", mean)
    print("平方差:", variance)
    print("标准差:", standard_deviation)
