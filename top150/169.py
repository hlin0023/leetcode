
def majorityElement(nums):
    maps = {}
    for i in range(len(nums)):
        if nums[i] in maps:
            maps[nums[i]] += 1
        else: 
            maps[nums[i]] = 1
    print(maps)

    for j in maps:
        if maps[j] > len(nums)/2:
            return j
        


if __name__ == "__main__":
    nums = [3,3,4]
    print(majorityElement(nums))