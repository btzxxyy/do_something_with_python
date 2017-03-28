#!/usr/bin/env python
# coding: utf-8
# copyRight by heibanke

import unittest
import re


class TestEmailRe(unittest.TestCase):
    def setUp(self):
        # You can add your true test case in true_test list
        # 邮箱名是英文字母，数字或者横线-，下划线_，并没说不能开头
        # 后缀网名可以是英文字母，数字
        # 域名可以是com，org，edu
        self.true_test = ['abc123@163.com',
                          'd_ff@baidu.org',
                          '-ff-@163.org',
                          '_ff_@163.org',
                          '----ff13---@163.org',
                          '__ff---@163.org',
                          '--ff__@163.org',
                          '123ff-__@163.org',
                          'ff--__123@163.org',
                          '----@163.edu',
                          '____@163.edu',
                          '1234@163.edu',
                          '-ff-@163.edu',
                          '-ff-@163.org',
                          '-ff-@fdsa.org',
                          '-ff-@163ff.org',
                          '-ff-@aa163.org',
                          '-ff-@a1.org',
                          '-ff-@1.org']
        # You can add your false test case in false_test list
        self.false_test = ['aabb',
                           '11aa@ff.com11',
                           'ff@ee',
                           '-ff-@1-63.org',
                           '-ff-@16 3.org',
                           '-ff-@16_3.org',
                           '-ff-@163.11org',
                           '-ff-@163.ddd',
                           '-ff-@163.212',
                           '-ff-163.org',
                           '-ff-@163.ceo',
                           '-----#@163.org']
        # you can input your pattern, this pattern is wrong
        self.pattern = re.compile(r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.(com|org|edu)$')

    def test_true(self):
        for t in self.true_test:
            if not self.pattern.match(t):
                assert False, "True list fail %s" % (t)
            else:
                a = self.pattern.match(t)
                print(a.groups())

    def test_false(self):
        for t in self.false_test:
            if self.pattern.match(t):
                a = self.pattern.match(t)
                print(a.groups())
                assert False, "False list fail %s" % (t)


if __name__ == "__main__":
    unittest.main()
