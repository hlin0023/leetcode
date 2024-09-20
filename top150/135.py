def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    print(ratings)
    candys_lst = [1] * len(ratings)
    # right check 
    for i in range(0, len(ratings) - 1):
        if ratings[i] > ratings[i+1] and not (candys_lst[i] > candys_lst[i+1]):
            candys_lst[i] +=  1
        elif ratings[i] < ratings[i+1] and not (candys_lst[i] < candys_lst[i+1]):
            candys_lst[i+1] = candys_lst[i] + 1
    print(candys_lst)
    #left check 
    for i in range(len(ratings)-1, 0, -1):
        if ratings[i] > ratings[i-1] and not (candys_lst[i] > candys_lst[i-1]):
            candys_lst[i] += candys_lst[i-1] + 1
        elif ratings[i] < ratings[i-1] and not (candys_lst[i] < candys_lst[i-1]):
            candys_lst[i - 1] = candys_lst[i] + 1
    print(candys_lst)
    return sum(candys_lst)

if __name__ == "__main__":
    # ratings = [1,0,2]
    #ratings = [1,2,87,87,87,2,1]
    ratings = [1,6,10,8,7,3,2]
    print(candy(ratings))
