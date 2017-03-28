#!/usr/bin/env python
# coding=utf-8
# 使用正则表达式验证email的合法性


def judge_email(s):
    import re
    p = re.compile(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.(?:com|org|edu)$')
    a = re.match(p, s)
    if a:
        return a.group() + ' is valid.'
    else:
        return s + ' is invilid.'

s = 'btzxxyy@163.com'
print(judge_email(s))

x = '12jr5ij@jpegji.com111'
print (judge_email(x))

