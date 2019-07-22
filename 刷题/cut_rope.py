def judge(x,nums):
	sum = 0
	for i in nums:
		sum += i // x
	return sum

	
def cut_rope(n,m,nums):
	left = 0
	right = max(nums)
	while right -left > 1e-9:
		mid = (left + right) / 2
		cut_num = judge(mid,nums)
		if cut_num >= m:
			left = mid
		else:
			right = mid
	return format(right,'.2f')


if __name__ == '__main__':
	print(cut_rope(4,11,[8.02,7.43,4.57,5.39]))
	print(cut_rope(3,4,[3,4,5]))