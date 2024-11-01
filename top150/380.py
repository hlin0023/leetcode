class RandomizedSet(object):

    def __init__(self):
        self.table ={}
        self.nums = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.table:
            return False
        self.table[val] = len(self.nums)
        self.nums.append(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.table:
            return False

        index = self.table[val]
        swap_v = self.nums[-1]
        self.nums[index] = swap_v# swap value
        self.table[swap_v] = index #replace the last value with val 
        del self.table[val]
        self.nums.pop() # delect the val in the end 
        return True

        

    def getRandom(self):
        """
        :rtype: int
        """
        return choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()