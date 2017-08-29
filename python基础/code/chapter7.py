# -*- coding: utf-8 -*-
# @Author: 28906
# @Date:   2017-08-29 09:33:17
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-08-29 11:02:41

## 异常处理综合案例

# 自定义一个异常类

class Error(Exception):
	'''这是一个所有自定义异常都可以继承的基类'''
	pass

# 超重的异常
class TooLangError(Error):
	def __init__(self, expression, message):
		self.expression = expression
		self.message = message
	def __str__(self):
		return repr(self.message)
# 计算平均每样商品的价格
def _cal_ava_price(total_price, total_num):
	return total_price/total_num

param = [
	{
	'name':'肉',
	'price':'15',
	'weight':'3'
	},
	{
	'name':'苹果',
	'price':8,
	'weight':'3'
	},
	{
	'name':'青菜',
	'price':'2',
	'weight':'12'
	}
]

## 超市结账系统
def super_cal(t):
	if t:
		try:
			flag = True
			# 总价
			total_price = sum(float(i['weight']) * float(i['price']) for i in t)
			# 总重
			total_num = sum(float(j['weight']) for j in t)
			# 单位价格
			per_price = _cal_ava_price(total_price,total_num)

			if total_num>10: # 超过10斤，提示东西买的太多了。不会做生意就这样。
				flag = False
				raise TooLangError(expression=None, message='东西买太多了')
		except TypeError as e:
			print('貌似类型出现异常了哦')		
		except TooLangError as e:
			print(e.message)
		except:
			print('这是一个漏网的异常')
			raise
		else:
			print('总价：{}，平均单价：{:.3f}'.format(total_price, per_price))
		finally:
			str = '欢迎再次光临' if flag else '请检查输入'
			print(str)


super_cal(param) 