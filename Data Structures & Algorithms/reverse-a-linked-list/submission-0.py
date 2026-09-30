# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = head
        head = head.next
        prev.next = None
        while head.next:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        head.next = prev
        return head
            