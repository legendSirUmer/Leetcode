import typing as tp
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if(l1.next is None and l2.next is None):
            return ListNode(l1.val + l2.val)
        elif(l1.next is None):
            return ListNode(l1.val + l2.val, self.addTwoNumbers(ListNode(0), l2.next))
        elif(l2.next is None):
            return ListNode(l1.val + l2.val, self.addTwoNumbers(l1.next, ListNode(0)))


    
        