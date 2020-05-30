# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0
        def sumGrandChilren(node):
            if node.left:
                print(1 + node.left.left.val)
                if node.left.left.val and node.left.left.val % 2 == 0:
                    self.sum += node.left.left.val
                if node.left.right.val and node.left.right.val % 2 == 0:
                    self.sum +=node.left.right.val
            if node.right:
                if node.right.left.val and node.right.left.val % 2 == 0:
                    self.sum += node.right.left.val
                if node.right.right.val and node.right.right.val % 2 == 0:
                    self.sum += node.right.right.val
        
        
        def treeRoot(node):
            if node.val:
                if node.val % 2 == 0:
                    sumGrandChilren(node)
                if node.left:
                    treeRoot(node.left)
                if node.right:
                    treeRoot(node.right)
        treeRoot(root)
        return self.sum

