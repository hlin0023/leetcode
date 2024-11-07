class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r = [1]*len(nums), [1]*len(nums)

        for i in range(1, len(nums)):
            l[i] = l[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]
        ans = []
        for i in range(len(nums)):
            ans.append(l[i] * r[i])
        return ans
    
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    a = Solution()
    print(a.productExceptSelf(nums))