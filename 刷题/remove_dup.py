def removeDuplicates(nums):
    if nums == []:
        return 0
    j = 0
    for i in range(0,len(nums)):
        if nums[i] != nums[j]:
            nums[j+1],nums[i] = nums[i],nums[j+1]
            j += 1
            print(i,j,nums)
    return j+1
if __name__ == '__main__':
    a = removeDuplicates([1,1,2])
    print(a)