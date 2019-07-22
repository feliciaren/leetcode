
def b_search(nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def intersect( nums1, nums2):
    nums2.sort()
    result = []
    for i in range(len(nums1)):
        if b_search(nums2,nums1[i]):
            # print('--')
            result.append(nums2.pop(b_search(nums2,nums1[i]) - 1))
    return result

if __name__ == '__main__':
	print(intersect([1,2,2,1],[2,2]))
