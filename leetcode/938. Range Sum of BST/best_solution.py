# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sum = 0
        def bst(root):
            if root:
                if root.val <= R and root.val >= L:
                    self.sum += root.val
                if root.left and root.val > L:
                    bst(root.left)
                if root.right and root.val < R:
                    bst(root.right)
        bst(root)
        return self.sum
        