def rotate_(nums, k):
    """
    Althought this list is not use extra space to store list, but... 
    This one is not passed with the long case if list is huge 
    """
    for i in range(len(nums) - 1, len(nums) - k - 1 , -1 ):
        temp_num = nums[-1]
        for j in range(len(nums) - 1, -1, -1 ):
            # print(i ,j)
            nums[j] = nums[j - 1]
        nums[0] = temp_num
    # print(nums)
       
def rotate(nums, k):
    new_lst = [-1] *len(nums)
    for i in range(len(nums)):
        print((i + k) % len(nums))
        # use the idea of the mod to shift, speed up the time 
        new_lst[(i + k) % len(nums)] = nums[i]
    nums = new_lst.copy()
    print(nums)
   

if __name__ == "__main__":
   nums =[1,2,3,4,5,6,7]
   k = 3
   rotate(nums, k)