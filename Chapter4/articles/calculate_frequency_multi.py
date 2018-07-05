#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: calculate_frequency_multi.py
"
"        Author: xss - callmexss@126.com
"   Description: ---
"        Create: 2018-07-06 00:07:10
"""""""""""""""""""""""""""""""""""""""""""""""

import os
import time
import string
import multiprocessing as multi

# from theading import Thread, Lock
from pprint import pprint
from collections import Counter


files = [f for f in os.listdir() if f.endswith('txt')] * 5

contents = []
new_words = []
mutex = multi.Lock()
punc = string.punctuation

def readFile(filename):
    time.sleep(0.1)
    print('current process id is', os.getpid())

    with open(filename, 'r') as f:
        mutex.acquire()
        contents.append(''.join(f.readlines()))
        mutex.release()
        

# 创建进程池
pool_num = 16
pool = multi.Pool(pool_num)

start = time.time()
cc = pool.map(readFile, files)
end = time.time()

print(contents)

contents_str = ''.join(contents)
print(contents_str)

words = contents_str.split(' ')
print(words)
for word in words:
    if not word:
        continue
    if word[-1] in punc:
        new_words.append(word[:-1])
    else:
        new_words.append(word)

most_common_ten = Counter(new_words).most_common(10)
pprint(most_common_ten)
