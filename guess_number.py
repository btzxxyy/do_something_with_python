#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/4 21:02
# @Author  : btzxxyy
# @Site    : 
# @File    : guess_number.py
# @Software: PyCharm

import random


def guess_number(ans):
    times = 6
    while(times > 0):
        try:
            get_number = int(input("Please input a number between 1 and 100: "))
            if 0 > get_number or get_number > 100:
                print("超出范围")
            else:
                if get_number == ans:
                    print("You win!")
                    break
                else:
                    print("bigger" if ans < get_number else "smaller")

            times -= 1
            if times == 0:
                print("you lose, the answer is " + str(ans) + ", try again")
        except:
            print("Invalid input.")
            times -= 1


if __name__ == '__main__':
    ans = random.randint(1, 100)
    guess_number(ans)


