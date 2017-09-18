# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-08-31 10:52:31
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-18 21:05:43

# 单元测试案例
from chapter9 import aver

import unittest

class TestChapter9AverFunction(unittest.TestCase):
	def test_aver(self):
		self.assertEqual(aver(1,2,3), 2.0)
		self.assertEqual(round(aver(1,3,7),1),3.7)
		self.assertRaises(ZeroDivisionError, aver)
		self.assertRaises(TypeError, aver, '')

if __name__ == '__main__':
	unittest.main()
