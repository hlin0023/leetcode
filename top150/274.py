class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        n = len(citations)
        # index = 0
        for i in range(n):
            # if n - i >= citations[i] and citations[i] > index:
            if n - i <= citations[i]: 
                return n - i

        return 0





if __name__ == "__main__":
    nums = [3,0,6,1,5]
    a = Solution()
    ans = a.hIndex(nums)
    print(ans)