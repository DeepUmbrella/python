
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# 环形车辆 减速 模型


def clip(x, max_value):
    for i in range(len(x)):
        if x[i] >= max_value:
            x[i] %= max_value


if __name__ == "__main__":

    path = 5000
    n = 100
    v0 = 50
    p = 0.3
    times = 3000

    np.random.seed(0)

    x = np.random.rand(n) * path
    x.sort()

    v = np.tile([v0], n).astype(np.float64)

    plt.figure(figsize=(9, 7), facecolor='w')

    for t in range(times):
        plt.scatter(x, [t]*n, s=1, c="k", alpha=0.05)
        for i in range(n):
            if x[(i+1) % n] > x[i]:
                d = x[(i+1) % n] - x[i]
            else:
                d = path - x[i] + x[(i+1) % n]
            if v[i] < d:
                if np.random.rand() < p:
                    v[i] += 1
                else:
                    v[i] -= 1
            else:
                v[i] = d - 1
        v = v.clip(0, 150)
        x += v
        clip(x, path)

    plt.xlim(0, path)
    plt.ylim(0, times)
    plt.xlabel("Cars Position", fontsize="14")
    plt.ylabel("Times", fontsize="14")
    plt.title("Circular Road", fontsize="16")
    plt.tight_layout(pad=2)
    plt.show()
