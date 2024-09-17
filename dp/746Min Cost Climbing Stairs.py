#746. Min Cost Climbing Stairs


cost = [1,100,1,1,1,100,1,1,100,1]\
#cost = [10,15,20]
def mincost(cost):
    l = len(cost)
    dp = [0] * l

    for i in range(l-2, -1, -1):
        print(i)
        print(cost[i])
        if (i == l - 2) :
        ##  Base case (n <= 2)
            # when n = 2 (n is total num of stars)
            if cost[i] > cost[i+1] :
                # climb 1 step > climb 2
                dp[i] =  cost[i+1]
                # dp take the last step (climb 2)
            else:
                dp[i] = cost[i]
                # dp take current value
        ##  NOT - Base case (n>3)
        else:
            if (cost[i] + dp[i+1]) > (cost[i+1] + dp[i+2]):
                # climb 1 step > climb 2
                # dp is the previous data storage 
                dp[i] = dp[i+2] + cost[i+1]
            else:
                dp[i] = dp[i+1] + cost[i]
        print(dp)


print(mincost(cost))