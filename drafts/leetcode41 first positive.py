"""
输入: [7,8,9,11,12]
输出: 1
"""

def firstPositive(nums):
    i = 1
    while i in nums:
        i += 1
    return i


nums = [7,8,9,11,12]
nums2 = [1,2,0]
print(firstPositive(nums))