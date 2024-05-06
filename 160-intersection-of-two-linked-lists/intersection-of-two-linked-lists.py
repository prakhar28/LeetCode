# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA = headA
        listB = headB

        if not headA or not headB:
            return None
            
        while listA != listB:
            if not listA:
                listA = headB
            else:
                listA = listA.next

            if not listB:
                listB = headA
            else:
                listB = listB.next
            
            if listA == listB:
                return listA
        
        return listA


