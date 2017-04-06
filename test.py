#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/4 20:41
# @Author  : btzxxyy
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from mytools import my_time

start_time = my_time.start_time()
li = []
for i in range(10000000):
    li.append(i ** 0.5)
end_time = my_time.end_time()

print(my_time.cal_time(start_time, end_time))