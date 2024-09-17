"""
nums = [10,9,2,5,3,7,101,18] Output: 4
nums = [1, 5, 2, 4, 3] Output: 3

"""

def incresing_sequence_aux(nums, i):
    if i == len(nums):
        return 1
    
    max_len = 1
    for j in range(i+1, len(nums)):
        #print(nums[i], nums[j])
        if nums[j] > nums[i] :
            max_len = max(max_len, incresing_sequence_aux(nums, j) + 1)
    return max_len   

def incresing_sequence(nums):
    """
    Time complexity: O(2^n * n) exponetional 
        - num of sequence -> O(2^n) 
        - travese each sequence for O(n) times
    """
    return max(incresing_sequence_aux(nums, i) for i in range(len(nums)))

## Optimised method -> use memory to store the results 
## Dynamic programming - recuresion with memeory - pruning
memo = {}
def incresing_sequence_dictionary_aux(nums, i):
    # O(logn)
    if i in memo:
        return memo[i]
    
    if i == len(nums):
        return 1
    
    max_len = 1
    for j in range(i+1, len(nums)):
        #print(nums[i], nums[j])
        if nums[j] > nums[i] :
            max_len = max(max_len, incresing_sequence_dictionary_aux(nums, j) + 1)
    memo[i] = max_len
    return max_len  

def incresing_sequence_dictionary(nums):
    """
    O(nlogn)
    """
    return max(incresing_sequence_dictionary_aux(nums, i) for i in range(len(nums)))

## Iteration - NON- recursive method

def incresing_sequence_iteration(nums):
    """
    O(n^2)
    
    """
    n = len(nums)
    memo_lst = [1] * n

    for i in reversed(range(n)):
        # print(nums[i])
        for j in range(i + 1, n):
            # print(nums[i],nums[j])
            if nums[j] > nums[i]:
                memo_lst[i] = max(memo_lst[i], memo_lst[j] + 1)
    # print(memo_lst)
    return max(memo_lst)
    
import copy
def maximum_subarray(nums):

    current_sum = max_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


nums = [5,4,-1,7,8]

print(maximum_subarray(nums))