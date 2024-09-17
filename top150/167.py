
def twoSum(numbers, target):
    for i in range(len(numbers)):
        if (target - numbers[i]) in numbers:
            print(i, target, target-numbers[i], numbers)
            if numbers[i] == target - numbers[i]:
                temp_lst = numbers[i+1::]
                print(temp_lst)
                res = temp_lst.index(target - numbers[i])+1 
                print(i+1, res)
                return [i+1, i+1+res]
            return [i+1, numbers.index(target - numbers[i])+1]

if __name__ == "__main__":
    numbers = [1,2,3,4,4,9,56,90]
    target = 8
    print(twoSum(numbers, target))