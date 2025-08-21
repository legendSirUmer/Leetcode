# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, List
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = []
        if not list1:
            return list2
        if not list2:
            return list1
        if not list1 and not list2:
            return []
        else:
             i = j = 0
             while i == (max(len(list1),len(list2))) or j == (max(len(list1),len(list2))):
                if(list1.next and list2.next):
                    if (list1[i] == list2[j]):
                        answer.append(list1[i])
                        i = i+1
                        j = j+1

                    elif(list1[i] > list2[j]):
                        answer.append(list2[j])
                        j = j+1
                    elif(list1[i] < list2[j]):
                        answer.append(list1[i])
                        i = i+1
        print(answer)
        return answer
    

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = []
        if not list1:
            return list2
        if not list2:
            return list1
        if not list1 and not list2:
            return []
        else:
             i = j = 0
             while list1.next or list2.next:
                 if(list1.val == list2.val):
                     answer.append(list1.val)
                     list1 = list1.next
                     list2 = list2.next

                 elif(list1.val > list2.val):
                     answer.append(list2.val)
                     list2 = list2.next

                 elif(list1.val < list2.val):
                     answer.append(list1.val)
                     list1 = list1.next
        return answer



                
            
                     
        
        




sol =Solution()
print(sol.mergeTwoLists2([1,2,4],[1,3,4]))
