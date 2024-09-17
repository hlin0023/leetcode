def max_value(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    
    # 初始化第一行和第一列
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    print(dp)
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    print(dp)
    # 动态规划计算中间格子的最大价值
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
            print(dp)
    return dp[-1][-1]

# 示例用法
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(max_value(grid))  # 输出 12
