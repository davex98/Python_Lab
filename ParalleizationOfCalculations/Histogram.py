from fast_histogram import histogram2d
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import numpy as np


class Histogram():
    def __init__(self, threads, data):
        self.threads = threads
        self.data = data

    def count(self):
        with ThreadPoolExecutor(self.threads) as e:
            ch = self.data.shape[1] // self.threads
            ch0 = [self.data[0, i * ch:(i + 1) * ch] for i in range(self.threads)]
            ch1 = [self.data[1, i * ch:(i + 1) * ch] for i in range(self.threads)]
            func = partial(histogram2d, bins=200, range=((-10, 10), (-10, 10)))
            results = e.map(func, ch0, ch1)
            output = sum(results)
            self.display(output)

    def display(self, n):
        x = np.linspace(np.min(self.data), np.max(self.data), 200)
        y = n[0, :]
        plt.bar(x, y)
        plt.show()


if __name__ == '__main__':
    h = Histogram(4, np.random.normal(0, 10, [2, 1000000]))
    h.count()

