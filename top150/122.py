class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profits += (prices[i+1] - prices[i])
        return profits



if __name__ == "__main__":
    prices = [1,2,3,4,5]
    a = Solution()
    ans = a.maxProfit(prices)
    print(ans)