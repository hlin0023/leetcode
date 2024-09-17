
"""
算法题用动态规划求K数， 
给一个数组，找出这样一些数，这个数字的左边的数都比他小， 右边的数都比他大 

"""

def findSpecialNumbers(nums):
    n = len(nums)
    left_max = [0] * n
    right_min = [0] * n
    
    # 计算每个位置左侧的最大值
    left_max[0] = nums[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], nums[i])

    
    # 计算每个位置右侧的最小值
    right_min[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], nums[i])
    print(left_max)
    print(right_min)
    # 检查每个位置是否符合条件
    result = []
    for i in range(n):
        if nums[i] >= left_max[i] and nums[i] <= right_min[i]:
            result.append(nums[i])
    
    return result

# 示例用法
nums = [1, 4, 3, 7, 10, 11, 12, 13]
result = findSpecialNumbers(nums)
print(result)  
