nums1 = [1, 2, 2, 1]
nums2 = [2]


# if (len(nums1) > len(nums2)):
#     nums1, nums2 = nums2, nums1

o = []
for i in nums1:
    if (i in nums2):
        o.append(i)
        nums2.remove(i)

print(o)
