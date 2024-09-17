def removeElement(nums, val):
    # n = len(nums)
    i =0 
    k = len(nums) 
    print(nums)
    while i < k :
        # print(nums)
        if k > i and nums[i] == val:
            nums.append(nums.pop(i))
            print(i, nums)
            k -= 1
            i -= 1
        print(i,k , nums)
        i += 1
    return k 

if __name__ == "__main__":
    nums = [2]
    val = 3
    print(removeElement(nums, val))