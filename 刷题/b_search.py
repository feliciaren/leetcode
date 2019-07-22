def b_search(nums,target):
	left = 0
	right = len(nums) - 1
	while left <= right:
		mid = (left + right) // 2
		# print(left,mid,right)
		if nums[mid] == target:
			return mid
		elif nums[mid] > target:
			right = mid - 1 
		else:
			left = mid + 1
	return False

def merge(nums1,nums2):
	result = []
	i = 0
	j = 0
	while i < len(nums1) and j < len(nums2):
		if nums1[i] <= nums2[j]:
			result.append(nums1[i])
			i += 1
		else:
			result.append(nums2[j])
			j += 1
	if i < len(nums1):
		result.extend(nums1[i:])
	if j < len(nums2):
		result.extend(nums2[j:])
	return result

def merge_sort(nums):
	if len(nums) == 1:
		return nums
	mid = (0 + len(nums)) // 2
	left = merge_sort(nums[:mid])
	right = merge_sort(nums[mid:])
	return merge(left,right)

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
	print(b_search([1,2,3,4,5],2.5))
	print(merge_sort([3,1,2,4,5]))
	print(quick_sort([2,3,1,4,5]))