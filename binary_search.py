#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:HW 
@file: binary_search.py 
@time: 2018/06/08 
"""



def binary_search(num_list , key):
	"""
	首先判断关键字是否存在有序序列中，如果不存在直接返回不存在
	 如果存在就进入循环体先得到序列的索引范围从0到序列的最大长度
	 然后得到序列中间索引，如果查找到的数字与序列中间值相等就直接返回中间的索引值
	 如果数字小于序列中间值就说明这个数字是在序列0到中间值的范围，然后将索引最大值设置为中间值减1，这样就设定了下次循环索引的范围
	 如果数字大于系列中间值就说明数字是序列中间值到最大值的范围，然后将索引最小值设置为中间值加1，设置下次循环的索引范围
	 一直循环直到序列的中间索引与数字相等并返回索引值
	:param num_list: 接受的有序list
	:param key: 查找的关键字
	:return: list查找的的索引值
	"""
	min = 0
	max = len(num_list)-1
	if key in num_list:
		while True:
			center = int((min+max)/2)
			if num_list[center] == key:
				return center
				max = center-1
			elif key > num_list[center]:
				min = center+1
	else :
		return "没有找到"

def recursion_binary_search(num_list , key , max , min=0):
	"""
	 首先判断关键字是否存在有序序列中，如果不存在直接返回不存在
	 如果存在就进入循环体先得到序列的索引范围从0到序列的最大长度
	 然后得到序列中间索引，如果查找到的数字与序列中间值相等就直接返回中间的索引值
	 如果数字小于序列中间值就说明这个数字是在序列0到中间值的范围，然后将索引最大值设置为中间值减1，这样就设定了下次循环索引的范围
	 如果数字大于系列中间值就说明数字是序列中间值到最大值的范围，然后将索引最小值设置为中间值加1，设置下次循环的索引范围
	 一直循环直到序列的中间索引与数字相等并返回索引值
	:param num_list: 接受的有序list
	:param key: 查找的关键字
	:param max: list最大索引范围
	:param min: list最小索引范围
	:return: list查找的的索引值
	"""
	if key in num_list:
		while True:
			center = int((min+max)/2)
			if num_list[center] == key:
				return center
			elif key < num_list[center]:
				max = center-1
				return recursion_binary_search(num_list , key ,  max , min)
			elif key > num_list[center]:
				min = center+1
				return recursion_binary_search(num_list , key ,  max , min)
	else :
		return "没有找到"


num_list = [1,2,3,5,6,7,9,10,11]

while True:
	key = input("请输入想要查找的数字或按q退出")
	if key =="q":
		break
	if key.isdigit():
		"""调用递归二分法"""
		# res = recursion_func(num_list,int(key),len(num_list)-1,)
		res = binary_search(num_list,int(key))
		if res == "没有找到":
			print ("输入的数字不存在，请重新输入")
		else:
			print ("您要查找的数字的索引是在列表num_list的%s位置"%res)
	else :
		print ("您输入的不是数字请重新输入！")
