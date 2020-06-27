# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.nums = []
        self.newTreeList = []
        def extractNums(root):
            self.nums.append(root.val)
            if root.right:
                extractNums(root.right)
            if root.left:
                extractNums(root.left)
        extractNums(root)
        self.nums = sorted(self.nums, reverse=True)
        self.numsLength = len(self.nums)
        def newTree(root):
            i=0
            val = 0
            while i <= self.numsLength-1 and root.val <= self.nums[i] :
                val +=self.nums[i]
                i +=1
            root.val = val
            if root.left:
                newTree(root.left)
            if root.right:
                newTree(root.right)
        newTree(root)
        return root