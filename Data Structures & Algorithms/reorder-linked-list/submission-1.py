# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        st = deque()

        cur = head
        while cur:
            st.append(cur)
            cur = cur.next
        
        cur = head
        sz = len(st)//2
        for _ in range(sz):
            nxt = cur.next
            pp = st.pop()
            print(pp.val)
            cur.next = pp
            cur.next.next = nxt
            cur = cur.next.next
        
        cur.next = None




