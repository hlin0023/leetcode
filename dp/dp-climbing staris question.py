"""
The question only allows to climb one or two steps each time
and N is the levels of the stairs 


=> F(n) = F(n-1) + F(n-2) because only one or two steps allow 
F(0) = 1
F(1) = 1
F(2) = 2
"""

def num_stairs(n):
    dp = [0] * (n+1) 
    dp[0], dp[1] = 1, 1

    for i in range(2, n+1):
        # print(i)
        dp[i] = dp[i-1] + dp[i-2] 
    # print(dp)
    return dp[n]

print(num_stairs(5))

class Node:
    def __init__(self, data):
        self.l = None
        self.r = None
        self.data = data

class Btree:
    def __init__(self):
        self.root = Node(0)
    
    def add(self, node):
        if self.root.l is None:
            self.root.l = node
        else:
            self.root.r = node
        
    
b_tree = Btree()

def tree(n):
    for i in range(n):
        b_tree.add(Node(i+1))
        b_tree.add(Node(i+2))
    return b_tree
        
print(tree(2).root.r.l.data)
