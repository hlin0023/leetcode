"""
nums = [2, 7, 11, 15]
target = 9
"""

def twoSum(nums, target):
    for i, num in enumerate(nums):
        for j, num2 in enumerate(nums):
            if num + num2 == target:
                return i, j

def twoSumHash(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        # print(num_dict)
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

def twoSumPointer(nums, target):
    nums_with_index = [(num, index) for index, num in enumerate(nums)]
    # print(nums_with_index)
    nums_with_index.sort(key=lambda x:x[0])
    # print(nums_with_index)
    left, right = 0, len(nums) - 1
    # print(left, right)
    
    while left < right:
        current_sum = nums_with_index[left][0] + nums_with_index[right][0]
        if current_sum == target:
            return [nums_with_index[left][1], nums_with_index[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

nums = [2, 7, 11, 15]
target = 9
print(twoSumPointer(nums, target))  # 输出 [0, 1]

