class Solution(object):

    def canJump(self, nums):

        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0
        count = 0
        current_end = 0 
        for i in range(len(nums) -1 ):
            # if i is over than farthest -> stuck at some points
            # if i > farthest:
            #     return False
            farthest = max(farthest, i + nums[i])
            print(i, farthest)
            if i == current_end:
                count += 1
                current_end = farthest  # Move the end of the jump range to farthest

            # if farthest >= len(nums) - 1 :
            #     break
            
        return count


    

if __name__ == "__main__":
    # nums = [2,3,1,1,4]
    # nums = [3,2,1,0,4]
    nums = [1,2,3]
    a = Solution()
    ans = a.canJump(nums)
    print(ans)