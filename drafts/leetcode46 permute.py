
def permute(nums):
    n = len(nums)
    if n == 1:
        return [nums]
    result = []
    # 使用递归
    for elm in nums:
        # print(nums)
        temp = nums[:]
        temp.remove(elm)
        sub_result = permute(temp)
        # 怎么在sub_result上每个元素均加上当前子元素
        temp2 = []
        for i in sub_result:
            i.insert(0, elm)
            temp2.append(i)
        result += temp2
    return result

def permute2(nums):
    def backtrack(current_permutation, remaining_nums):
        # 当前排列长度等于原始数组长度时，表示找到一个完整排列
        if len(current_permutation) == len(nums):
            result.append(current_permutation[:])
            return
        for i in range(len(remaining_nums)):
            num = remaining_nums[i]
            current_permutation.append(num)  # 添加当前数字到排列中
            backtrack(current_permutation, remaining_nums[:i] + remaining_nums[i+1:])  # 递归处理剩余数字
            current_permutation.pop()  # 回溯，撤销选择的数字
    
    result = []
    backtrack([], nums)
    return result


if __name__ == "__main__":
    nums = [1,2,3]
    print(permute2(nums))
    #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]