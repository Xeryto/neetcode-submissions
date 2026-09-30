# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        st = []
        cur = head
        while cur:
            st.append(cur)
            cur = cur.next
        
        n = len(st)

        cur = head
        for i in range(n//2):
            nxt = cur.next
            bottom = st.pop(-1)
            cur.next = bottom
            bottom.next = nxt
            cur = nxt
        
        cur.next = None