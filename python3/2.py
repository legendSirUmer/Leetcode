import typing as tp
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tot = 0
        i = 0
        while(l1 or l2):
            if l1:
                tot += l1.val * (10 ** i)
                l1 = l1.next
                
            if l2:
                tot += l2.val * (10 ** i)
                l2 = l2.next

                
            i += 1

        print(tot)
        l_tot = ListNode(0)
        current = l_tot
        for c in str(tot)[::-1]:
            l_tot.next = ListNode(int(c))
            l_tot = l_tot.next

        return(current.next)
 


    
sol = Solution()

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

l3 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l4 = ListNode(9, ListNode(9, ListNode(9, ListNode(9,))))

print(sol.addTwoNumbers(l1,l2))
print(sol.addTwoNumbers(l3,l4))
