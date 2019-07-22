def findMedianSortedArrays(nums1,nums2):
    len1 = len(nums1)
    len2 = len(nums2)
    if len1 > len2:
        nums1,nums2 = nums2,nums1
    k = (len(nums1) + len(nums2)) // 2
    print(k)
    if len(nums1) == 0:
        return nums2[len(nums2)//2]
    while len(nums1)>=k >= 1:
        p1 = min(k//2,len(nums1))
        p2 = k-p1
        print(p1,p2,nums1,nums2)
        if nums1[p1-1]<=nums2[p2-1]:
            nums1 = nums1[p1:]
        else:
            nums2 = nums2[p2:]
        k = k // 2
    if (len1+len2)%2 == 1:
        return min(nums1[0],nums2[0])
    else:
        return (nums1[0]+nums2[0])/2
if __name__ == '__main__':
    nums1 = [1,3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1,nums2))