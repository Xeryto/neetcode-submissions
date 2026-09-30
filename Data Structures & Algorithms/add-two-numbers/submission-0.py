# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carryover = 0
        while l1 and l2:
            res, carry = (l1.val+l2.val+carryover)%10, math.floor((l1.val+l2.val+carryover)/10)
            carryover = carry
            node = ListNode(res)
            cur.next = node
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            res, carry = (l1.val+carryover)%10, math.floor((l1.val+carryover)/10)
            carryover = carry
            node = ListNode(res)
            cur.next = node
            cur = cur.next
            l1 = l1.next
        
        while l2:
            res, carry = (l2.val+carryover)%10, math.floor((l2.val+carryover)/10)
            carryover = carry
            node = ListNode(res)
            cur.next = node
            cur = cur.next
            l2 = l2.next
        
        if carryover != 0:
            node = ListNode(carryover)
            cur.next = node
        
        return dummy.next