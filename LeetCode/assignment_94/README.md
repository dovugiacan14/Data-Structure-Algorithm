# Assignment 94: Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1: 
- Input: root = [1,null,2,3]
- Output: [1,3,2]

Example 2: 
- Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
- Output: [4,2,6,5,7,1,3,9,8]

**General Rules: 
The input list represents the tree in level-order traversal, meaning it is arranged level by level 
from top -> bottom, left -> right 
    + root[0] is the root. 
    + for each root[i]:
        ++ The left child is at root[2*i + 1]
        ++ The right child is at root[2*i + 2]
    + null indicates that the node does not exist. 

** Method 1: Use Recursive 
B1: If root is None -> Return []
B2: Call recursive with root.left and get the value of left child node  -> get root.val
B3: Call recursive with root.right and get the value of right child node -> get root.val 
B4: Return the list follow the order Left -> Root -> Right.

**Method 2: Use Stack 
B1: Traverse all the left branches and push them onto the stack
B2: Retrieve the value of the top node from the stack (root node)
B3: Continue traversing the right branch 
B4: Repeat until the stack is empty and there are no more nodes to traverse.
