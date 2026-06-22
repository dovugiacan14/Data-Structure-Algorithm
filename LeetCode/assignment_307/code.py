class NumArray(object): 
    def __init__(self, nums): 
        self.nums = nums 

    def update(self, index, val): 
        self.nums[index] = val  

    def sumRange(self, left, right): 
        new_sums = self.nums[left:right+1]
        return sum(new_sums) 


class NumArray(object): 
    def __init__(self, nums): 
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1) 

        for i, x in enumerate(nums): 
            self._add(i + 1, x) 
        
    def _add(self, i, delta): 
        while i <= self.n: 
            self.bit[i] += delta 
            i += i & -i

    def _prefix_sum(self, i): 
        res = 0 
        while i > 0: 
            res += self.bit[i]
            i -= i & -i
        return res

    def update(self, index, val): 
        delta = val - self.nums[index] 
        self.nums[index] = val 
        self._add(index + 1, delta) 

    def sumRange(self, left, right): 
        new_sums = self.nums[left:right+1]
        return sum(new_sums) 
