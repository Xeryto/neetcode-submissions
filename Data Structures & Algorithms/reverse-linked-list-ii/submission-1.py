# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = head

        if left == 1:
            prev = ListNode(-501, head)
        
        left_node = head
        for i in range(left-1):
            left_node = left_node.next
        

        for i in range(left-2):
            prev = prev.next
        
        
        if left == right:
            return head

        last = left_node
        cur = left_node
        nxt = left_node.next
        for _ in range(right-left):
            tmp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = tmp
        
        prev.next = cur
        if prev.val == -501:
            head = cur
        last.next = nxt

        return head
