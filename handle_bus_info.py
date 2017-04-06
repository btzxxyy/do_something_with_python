#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/29 19:07
# @Author  : btzxxyy
# @Site    : 
# @File    : handle_bus_info.py
# @Software: PyCharm

import csv
import pdb
import re

with open('beijing_jt.csv') as f:
    f_csv = f.readlines()

s_tmp = ''.join(f_csv[1:40])
a = s_tmp.split(',')
station_info = a[-1].split('\n \n')
p = re.compile(r'(?P<number>[0-9]+)\s(?P<name>\D+)\s')
final = {}
# for i in station_info:
    # temp = re.match(p_title, i)
    # if temp:
    #     print(temp.group())
        # final[stations[0]] = stations[1]
        # stations = re.match(p, i)
        # if stations:
        #     print(stations.group())


