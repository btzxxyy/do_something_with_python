#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

from __future__ import print_function

s = "afAzfdfjdBHSD"

# AaBbCcDd

s_lst = list(s)

sort_lst = sorted(s_lst, cmp=lambda x, y: ord(x)-ord(y))

print(s)

print(''.join(sort_lst))
