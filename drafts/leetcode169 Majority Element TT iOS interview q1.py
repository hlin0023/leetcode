"""
[1,2,3,2,2,2,5,4,2]
2 repeated for 5 times
return 2 
"""
def find_majority(nums):
    major_dic = {} # O(n)
    for i in range(len(nums)):
        if nums[i] in major_dic: #O(1) for Dictionary
            major_dic[nums[i]] += 1
        else:
            major_dic[nums[i]] = 1
    # print(max(major_dic))
    # return the key that got the largest counts
    print(max(major_dic))
    return max(major_dic, key=lambda key: major_dic[key]) if max(major_dic.values()) > len(nums)/2 else -1

#nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
nums = [2,2,1,1,1,2,2]
print(find_majority(nums))