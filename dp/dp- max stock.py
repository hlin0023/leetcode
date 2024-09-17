"""
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第2天（股票价格=1）的时候买入，在第3天（股票价格=5）的时候卖出，利润 = 5-1 = 4。
然后在第4天（股票价格=3）的时候买入，在第5天（股票价格=6）的时候卖出，利润 = 6-3 = 3。

"""

def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0
    
    n = len(prices)
    dp = [0] * n
    
    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            dp[i] = dp[i - 1] + prices[i] - prices[i - 1]
    print(dp)
    return sum(dp)

# 示例用法
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))  # 输出 7
