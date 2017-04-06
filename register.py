#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/4 21:44
# @Author  : btzxxyy
# @File    : register.py
# @Software: PyCharm

import re
import hashlib
import guess_number


def get_user_data():
    with open("userdata.txt", 'r') as f:
        data = f.readlines()

    s = "".join(data)

    d = {}
    li = s.split('\n')
    for each in li:
        if "username" in each:
            temp = each.split("\t")
            d[temp[0][10:]] = temp[1][10:]
    return d


def register():
    username = input("请输入用户名：")
    while 1:
        if username in get_user_data():
            print("用户名已存在,请更换用户名后重试！")
            break
        else:
            p = re.compile(r"^([a-z_])[a-zA-Z0-9_-]+$")
            if len(username) < 4:
                print("用户名太短了！至少需要四位！")
                continue
            if not re.match(p, username):
                print("用户名必须以小写字母开头，且只能包含数字、大小写字母、横线、下划线")
                continue
            while 1:
                password = input("请输入密码：")
                p = re.compile(r"^[a-zA-Z0-9_-]+$")
                if len(password) < 6:
                    print("密码太短了！")
                    continue
                if not re.match(p, password):
                    print("用户名必须以小写字母开头，且只能包含数字、大小写字母、横线、下划线")
                    continue
                break
        with open("userdata.txt", "a+") as f:
            f.write("username: " + username + "\t" + "password: " +
                    hashlib.md5(password.encode('utf-8')).hexdigest() + "\n")
        print(username + "已经创建成功。")
        break


def login():
    userdata = get_user_data()
    username = input("请输入用户名：")
    if username in userdata.keys():
        password = input("请输入密码：")
        if userdata[username] == hashlib.md5(password.encode('utf-8')).hexdigest():
            print("登陆成功")
            import random
            ans = random.randint(1, 100)
            guess_number.guess_number(ans)
    else:
        print("该用户名不存在")


if __name__ == '__main__':
    while 1:
        get_s = input('''
        input 'r' to register.
        input 'l' to login.
        input 'e' to exit.
        ''')
        if get_s.lower() == 'r':
            register()
        elif get_s.lower() == 'l':
            login()
        elif get_s.lower() == 'e':
            break
        else:
            print("Invalid Input!")
            break
