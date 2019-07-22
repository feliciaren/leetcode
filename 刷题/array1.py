# 考察一维数组
# 判断数组中是否存在重复数字，数组长度为n，里面存在n-1个数字在1~n-1之间 ，找出任意一个重复的数字
# 注意边界溢出的情况
def repeat_number(a):
# 穷举法，对每一个数字都遍历一遍数组
# 时间复杂度O(n^2),空间复杂度O(1)
	for i in range(len(a)):
		if a[i] >= len(a) or a[i] <= 0:
			print('Wrong Input')
			return None
	for i in range(len(a)):
		for j in range(i + 1, len(a), 1):
			if a[i] == a[j]:
				return a[i]

def repeat_number2(a):
# 建立一个哈希数组存储，对应第i个位置存第i个数
# 时间复杂度O(n)，空间复杂度O(n)
	for i in range(len(a)):
		if a[i] >= len(a) or a[i] <= 0:
			print('Wrong Input')
			return None
	repeat_a = [len(a)] * len(a)
	for i in range(len(a)):
		if repeat_a[a[i]] == len(a):
			repeat_a[a[i]] = a[i]
		else:
			return a[i]

def repeat_number3(a):
# 也可递归
# 长度为n的数组，放n-1个数，对于排序好的数组，没有重复数字的话应该第i个位置放第i个数,因此对不在位置的数交换位置
# 时间复杂度O(n)，空间复杂度O(1)
	for i in range(len(a)):
		if a[i] >= len(a) or a[i] <= 0:
			print('Wrong Input')
			return None
		# print(a)
	for i in range(len(a)):
		while a[i] != i:
			if a[a[i]] != a[i]:
				temp = a[a[i]]
				a[a[i]] = a[i]
				a[i] = temp
				# repeat_number3(a)
			else:
				return a[i]

import random

def count_number(number,l):
	result = 0
	for i in l:
		if number == i:
			result += 1
	return result

def repeat_number4(a):
# 可能会出现找不到答案的情况 找不到答案的原因：查找数字 + 查找数字重复的次数 = mid
# 未对数组进行修改，但是空间复杂度较低
# 时间复杂度O(nlogn):因为需要对1~n-1的数字做二分查找，复杂度为logn；每次需要遍历一遍数组，复杂度为n
# 不需要额外的空间，因此空间复杂度为O(1)
	for i in range(len(a)):
		if a[i] >= len(a) or a[i] <= 0:
			print('Wrong Input')
			return None
	left = 1
	right = len(a)
	mid = random.randint(left,right)
	while left < right:
		mid = random.randint(left,right)
		# print('mid',mid)
		# print('left',left)
		# print('right',right)
		count = 0
		for i in range(left, mid + 1, 1):
			count += count_number(i,a)
		# print('count',count)
		# print('mid',mid)
		if count > (mid - left + 1):
			right = mid	
		else:
			left = left + 1


	count = count_number(left,a)
	if count > 1:
		return left

if __name__ == '__main__':
	a = [2,3,1,3]
	print('穷举', repeat_number(a))
	print('哈希', repeat_number2(a))
	print('交换位置',repeat_number3(a))
	print('二分查找',repeat_number4(a))
	
