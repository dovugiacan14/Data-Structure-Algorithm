
class TreeNode(object): 
    def __init__(self, val, left, right): 
        self.val = val 
        self.left = left 
        self.right = right 

def sorted_array_to_bst(nums):
    if not nums: 
        return None 
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    root.left = sorted_array_to_bst(nums[:mid]) # build left subtree
    root.right = sorted_array_to_bst(nums[mid+1:]) # build right subtree

    return root 
