def quick_sort(nums):
	if len(nums) < 2:
		return nums
	else:
		left = []
		right = []
		pick = nums.pop(0)
		for i in nums:
			if i > pick:
				right.append(i)
			else:
				left.append(i)
		return quick_sort(left) + [pick] + quick_sort(right)
if __name__ == '__main__':
	print(quick_sort([3,5,7,8,2,5]))
