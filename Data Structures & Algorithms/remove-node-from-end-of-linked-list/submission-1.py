# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we need to move N-n from head
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # moves by n
        for i in range(n):
            right = right.next
        
        # moves by N-n
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next