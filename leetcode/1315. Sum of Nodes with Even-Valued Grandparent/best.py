# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        
        def dfs(node, parent, grandparent):
            # Check whether parent of the next nodes we are going to call dfs on is even
            p = node.val % 2 == 0
            # Parent of this node is the grandparent of the next nodes we are going to call dfs on
            g = parent
            if grandparent:
                self.total += node.val
            if node.left:
                dfs(node.left, p, g)
            if node.right:
                dfs(node.right, p, g)
                
        
        dfs(root, False, False)
        
        return self.total