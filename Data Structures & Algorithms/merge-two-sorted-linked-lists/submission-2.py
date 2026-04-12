# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1, cur2 = list1, list2
        list3 = ListNode(0)
        cur3 = list3
        cur3.next = cur1 or cur2
        
        while cur1 is not None and cur2 is not None:
            if cur1.val < cur2.val:
                cur3.next = cur1
                cur1 = cur1.next
                cur3 = cur3.next
            elif cur1.val > cur2.val:
                cur3.next = cur2
                cur2 = cur2.next
                cur3 = cur3.next
            else:
                cur3.next = cur1
                cur1 = cur1.next
                cur3 = cur3.next
        if cur1 is None:
            cur3.next = cur2
        if cur2 is None:
            cur3.next = cur1
        return list3.next
        