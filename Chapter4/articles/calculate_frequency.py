#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: calculate_frequency.py
"
"        Author: xss - callmexss@126.com
"   Description: ---
"        Create: 2018-07-05 00:03:18
"""""""""""""""""""""""""""""""""""""""""""""""

import os
import string

from collections import Counter
from pprint import pprint


files = [f for f in os.listdir() if f.endswith('txt')]

contents = []

for f in files:
    with open(f, 'r') as f:
        contents.append(f.read())

contents_str = ''.join(contents)
punc = string.punctuation
words = contents_str.split(' ')
new_words = []

for word in words:
    if not word:
        continue
    if word[-1] in punc:
        new_words.append(word[:-1].lower())
    else:
        new_words.append(word.lower())
        
# pprint(set(new_words))

most_common_ten = Counter(new_words).most_common(10)
pprint(most_common_ten)
