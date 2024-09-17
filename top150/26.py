def removeDuplicates(nums):
    i, j = 0, 1
    while j < len(nums):
        if nums[i] == nums[j]:
            nums.remove(nums[j])
        else: 
            i += 1
            j += 1
    return len(nums)

if __name__ == "__main__":
    nums = [1, 1, 2]
    print(removeDuplicates(nums))