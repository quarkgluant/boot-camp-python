#!/usr/bin/env python3
# -*-coding:utf-8 -*

import time, os

def log(func):
    def wrapper(*args):
        start = time.time()
        original_result = func(*args)
        end = time.time()
        diff = end - start
        res = f"{diff:.03f} s" if diff > 0.01 else f"{(diff  * 1000):.03f} ms]"
        with open("machine.log", "a") as log_file:
            log_file.write(f"({os.getlogin()}) Running: {func.__name__}     [exec-time = {res}]\n")
        return original_result
    return wrapper

