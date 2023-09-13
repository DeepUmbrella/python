import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
import math


N = 1000

times = 100

z = np.zeros(N)

for i in range(times):
    z += np.random.rand(N)

z /= times

plt.hist(z, bins=20, color="m", edgecolor="k")

plt.show()


d = np.random.rand(10)

print(d)

d[d < 0.5] = 0.5

print(d)


# numpu y =x^x

x = np.arange(0, 10, 1)

x = np.linspace(0, 1, 100)

y = x**x


plt.plot(x, y, "r-", linewidth=2)


plt.show()


# 分类器
# 计算一个每个都独立有0.6的概率做出正确选择  一个概率为0.4 并且少数服从多数的分类器


def classify(x: int, rate: float):
    # 向上取整 rate
    s = 0
    for i in range(x//2 + 1, x+1):
        s += comb(x, i) * rate**i * (1-rate)**(x-i)
    return s


rate = classify(10, .6)


print(rate)
