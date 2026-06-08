from collections import deque

def pathSum(root, targetSum):
    if not root: 
        return []
    result = []

    def process(node, target, tmp_val_lst, curr_sum):
        tmp_val_lst.append(node.val)
        curr_sum += node.val 

        if not node.left and not node.right and curr_sum == target: 
            result.append(list(tmp_val_lst))

        process(node.left, target, tmp_val_lst, curr_sum)
        process(node.right, target, tmp_val_lst, curr_sum)

        tmp_val_lst.pop()
    
    process(root, targetSum, [], 0)
    return result
