class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 1:
            return [str(nums[0])]
        current = []
        res = []
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                print(current)
                if len(current) == 0:
                    current = [nums[i], nums[i+1]]
                else:
                    current[1] = nums[i+1]
            else:
                print(i, current)
                if len(current) == 2:
                    if current[0] == current[1]:
                        res.append(str(current[0]))
                    else:
                        res.append(str(current[0])+"->"+str(current[1]))
                else:
                    res.append(str(nums[i]))
                current = [nums[i+1], nums[i+1]]
        #handling the rest 
        print(current)
        if len(current) == 2:
            if current[0] == current[1]:
                res.append(str(current[0]))
            else:
                res.append(str(current[0])+"->"+str(current[1]))
            # print(res)
        # else:

        return res
if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    nums = [-1]
    # nums = [0,2,3,4,6,8,9]
    a = Solution()
    print(a.summaryRanges(nums))
