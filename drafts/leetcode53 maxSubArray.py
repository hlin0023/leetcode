def maxSubArray(nums):
    if not nums:
        return 0
    
    maxSum = nums[0] # 最大和初始化为第一个元素
    currentSum = nums[0] # 当前子数组和初始化为第一个元素
    
    for num in nums[1:]:
        print(num)
        # 如果当前子数组和为负数，则重新开始子数组
        currentSum = max(num, currentSum + num)
        # 更新最大和
        maxSum = max(maxSum, currentSum)

        print(currentSum, maxSum)
    return maxSum


def maxSubArray2(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    maxSum = dp[0]
    
    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
        maxSum = max(maxSum, dp[i])
    print(dp)
    return maxSum





nums = [3, -4, 2, -1, 2, 6, -5, 4]
print(maxSubArray2(nums))