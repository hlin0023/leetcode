def largestNumber(nums) -> str:
    s = ''
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if str(nums[i])+str(nums[j]) < str(nums[j])+str(nums[i]):
                nums[i],nums[j] = nums[j],nums[i]
    for x in (nums):
        s += str(x)
    return str(int(s))


if __name__ == "__main__":
    nums = [10,2]
    print(largestNumber(nums))