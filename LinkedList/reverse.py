class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class Solution:
    def reverse(self,head:ListNode,tail:ListNode,terminal:ListNode):