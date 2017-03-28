#!/usr/bin/env python
# coding=utf-8

import re

p = re.compile(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9-_]+\.(?:com|org|edu)$')
a = re.match(p, 'btzxxyy@163.com')
b = re.match(p, '12jr5ij@jpegji.com111')



def judge_email(s):
    import re
    p = re.compile(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9-_]+\.(?:com|org|edu)$')
    a = re.match(p, s)
    if a:
        return a.group() + ' is valid.'
    else:
        return s + ' is invilid.'

s = 'btzxxyy@163.com'
print(judge_email(s))

x = '12jr5ij@jpegji.com111'
print judge_email(x)

