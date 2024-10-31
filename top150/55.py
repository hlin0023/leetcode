class Solution(object):

    def canJump(self, nums):

        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0
        for i in range(len(nums)):
            # if i is over than farthest -> stuck at some points
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            print(i, farthest)
        return True


    

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    #nums = [3,2,1,0,4]
    a = Solution()
    ans = a.canJump(nums)
    print(ans)