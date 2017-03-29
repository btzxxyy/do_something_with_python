#!/usr/bin/env python
# coding=utf-8

from mytools import createstr
import random


def create_user_name(n=6):
    user_name = ['0'] * n
    begin = ['_'] + createstr.create_str('s')
    user_name[0] = random.choice(begin)
    for i in range(1, n):
        user_name[i] = random.choice(createstr.create_str('sd') + ['_'])
    return ''.join(user_name)


def create_user_pass(n=8):
    user_pass = ['0'] * n
    for i in range(0, n):
        user_pass[i] = random.choice(createstr.create_str('w'))
    return ''.join(user_pass)


if __name__ == '__main__':
    with open('userdata.txt', 'w') as f:
        count = 0
        while(count < 10):
            f.write('username: ' + create_user_name() + '\tpassword: ' +
                    create_user_pass() + '\n')
            count += 1