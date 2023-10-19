#!/bin/bash

import threading
import time

def task1():
    time.sleep(3)
    print('completed task 1')

def task2():
    time.sleep(4)
    print('completed task 2')

def task3():
    time.sleep(5)
    print('completed task 3')


x = threading.Thread(target=task1, args=())
x.start()

y = threading.Thread(target=task2, args=())
y.start()

z = threading.Thread(target=task3, args=())
z.start()

print(threading.active_count())
print(threading.enumerate())