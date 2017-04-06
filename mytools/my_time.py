#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/4 20:38
# @Author  : btzxxyy
# @Site    : 
# @File    : my_time.py
# @Software: PyCharm


import time


def start_time():
    return time.clock()


def end_time():
    return time.clock()

def cal_time(start_time, end_time):
    return end_time - start_time

