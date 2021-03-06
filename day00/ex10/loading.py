#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys
import time
from time import sleep


def ft_progress(list, prefix="", size=60, file=sys.stdout):
    count = len(list)
    start = time.time()

    def show(j):
        x = int(size * j / count)
        percent = j / count * 100
        total_time = (time.time() - start) * count if j == 0 else (time.time() - start) * (count / j)
        eta = abs(total_time - (time.time() - start))
        file.write("ETA: %02.2fs [%02.2f%s] %s[%s%s%s] %i/%i | elapsed time %02.2fs\r" % (
            eta, percent, "%", prefix, "=" * x, ">", " " * (size - x), j, count, (time.time() - start)))
        file.flush()

    show(0)
    for index, item in enumerate(list):
        yield item
        show(index + 1)
    file.write("\n")
    file.flush()


if __name__ == '__main__':
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)

    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
