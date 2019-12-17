#!/usr/bin/env python3
# -*-coding:utf-8 -*
from time import sleep

import ai42.progressbar
import ai42.logging.log

@log
def on_progresse:
    listy = range(3333)
    ret = 0
    for elem in progressbar(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)

if __name__ == '__main__':
    on_progresse()
