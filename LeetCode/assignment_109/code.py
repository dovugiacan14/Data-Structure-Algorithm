class TreeNode(object): 
    def __init__(self, val= 0, left= None, right= None): 
        self.val = val 
        self.left = left 
        self.right = right 
    
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sorted_list_to_bst(head): 
    if not head: 
        return None 

    # convert head to array 
    arr = []
    while head: 
        arr.append(head.val)
        head = head.next 

    def sorted_arr_to_bst(nums): 
        if not nums: 
            return None 
        mid = len(nums) // 2 
        root = TreeNode(nums[mid])

        root.left = sorted_arr_to_bst(nums[:mid])
        root.right= sorted_arr_to_bst(nums[mid + 1:])
        return root 
    
    return sorted_arr_to_bst(arr)
