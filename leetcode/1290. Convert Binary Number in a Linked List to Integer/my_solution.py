# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result=0
        self.ds = []
        
        def lister(num):
            if num:
                self.ds += [num.val]
                if num.next:
                    lister(num.next)
        lister(head)
        for i,digit in enumerate(self.ds[::-1]):
            result += (digit * (2**i))
        return result
