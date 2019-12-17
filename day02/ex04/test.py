#!/usr/bin/env python3
# -*-coding:utf-8 -*
from time import sleep

import ai42.progressbar
import ai42.logging.log

if __name__ == '__main__':
    @log
    listy = range(3333)
    ret = 0
    for elem in progressbar.ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)