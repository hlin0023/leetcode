
"""
find the sum of the first N numbers

f(i) is the sum of the first i elements 

f(n) = f(n-1) +n
"""
def fac(n):
    dp = [0] * (n+1)
    for i in range(1, n+1):
        # print(i)
        dp[i] = dp[i-1] + i
    # print(dp)
    return dp[n]


print(fac(10))
