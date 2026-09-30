# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        st = []
        cur = head
        while cur:
            st.append(cur)
            cur = cur.next
        
        if len(st) == n:
            return st[1] if len(st) > 1 else None
        
        nxt = None
        for i in range(n-1):
            nxt = st.pop(-1)
        
        node = st.pop(-1)
        prev = st.pop(-1)
    
        prev.next = nxt

        return head