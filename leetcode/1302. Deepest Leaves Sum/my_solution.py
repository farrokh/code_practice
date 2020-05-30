# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.dictionary = {}
        self.maxlevel = 1
        def deepestLeave(leave, level):
            level += 1
                
            if leave.left:
                deepestLeave(leave.left, level)
            if leave.right:
                deepestLeave(leave.right, level)

            if level in self.dictionary:
                self.dictionary[level] += leave.val   
                
            elif level not in self.dictionary:
                self.dictionary[level] = leave.val
            
            if level > self.maxlevel:
                self.maxlevel = level
               
        deepestLeave(root, 0)

        return self.dictionary[self.maxlevel]
