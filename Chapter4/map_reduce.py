#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: map_reduce.py
"
"        Author: xss - callmexss@126.com
"   Description: Function programming
"        Create: 2018-07-03 23:53:24
"""""""""""""""""""""""""""""""""""""""""""""""
try:
    import reduce  # for python2
except ImportError:
    from functools import reduce  # for python3

iter_li = map(lambda x: x ** 2, [x for x in range(1, 4)])
li = list(iter_li)
print(li)


def add(a, b):
    return a + b


sum_of_1_to_100 = reduce(add, range(1, 101))
print(sum_of_1_to_100)
