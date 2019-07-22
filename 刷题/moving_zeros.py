# def moving_zeros(nums):
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_loc = []
    for i in nums:
        if i == 0:
            zero_loc.append(0)
    for i in range(len(zero_loc)):
        nums.remove(0)
    nums.extend(zero_loc)
        

if __name__ == '__main__':
    nums = [0,0,1]
    moveZeroes(nums)
    print(nums)
    print(5//3)