from typing import List 

class NumArray: 
    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i, n in enumerate(nums): 
            self.prefix[i + 1] = self.prefix[i] + n 
    
    def sumRange(self, left: int, right: int): 
        return self.prefix[right + 1] - self.prefix[left]

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    num_array = NumArray(nums)
    print(num_array.sumRange(0, 2))  
    print(num_array.sumRange(2, 5))  
    print(num_array.sumRange(0, 5)) 