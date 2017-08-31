# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-08-31 10:52:31
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-08-31 11:00:02


from chapter9 import *

import unittest

class TestChapter9AverFunction(unittest.TestCase):
	def test_aver(self):
		self.assertEqual(aver(1,2,3), 2.0)
		self.assertEqual(round(aver(1,3,7),1),3.7)
		self.assertRaises(ZeroDivisionError, aver, 0)
		self.assertRaises(TypeError, aver, '')

	unittest.main()
