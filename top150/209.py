class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        ans = len(nums) + 1
        start, end = 0, 0
        sum = 0
        # nums = sorted(nums) #####//Mistaken//### 
        #this question is asking for sub array, not the mini array meets target
        # sorting will change the format resulting wrong 
        while end < len(nums):
            sum += nums[end] 
            while sum >= target :
                ans = min(ans, end - start +1)
                sum -= nums[start] # move start to the right - delect first 
                start += 1
            end += 1
        if ans == len(nums) + 1:
            return 0
        else:
            return ans
        
if __name__ =="__main__":
    target = 213
    nums = [12,28,83,4,25,26,25,2,25,25,25,12]
    a = Solution()
    print(a.minSubArrayLen(target, nums))
    