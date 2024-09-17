def removeDuplicates(nums):
    i, count = 0, 1
    length = len(nums)
    
    while i < length -1:
        if nums[i] == nums[i+1]:
            count += 1 
            i += 1
        else:
            count = 1
            i += 1
        if count > 2 :
            nums.pop(i)
            length -= 1
            count = 1
            i = 0 
    print(nums)  

    return len(nums)

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    removeDuplicates(nums)
