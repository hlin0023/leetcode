class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_buy = prices[0] 
        profit = 0
        for i in range(1, len(prices)):
            # print(min_buy, profit)
            if prices[i] - min_buy > profit :
                profit = prices[i] - min_buy
            # just handling the min before the current i     
            if prices[i] < min_buy:
                min_buy = prices[i]
            # print(min_buy)
        return profit
            

        







if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    a = Solution()
    ans = a.maxProfit(prices)
    print(ans)