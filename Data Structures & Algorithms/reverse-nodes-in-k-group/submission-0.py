# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = dummy.next
        
        while cur:
            st = []
            for i in range(k):
                if not cur:
                    break
                st.append(cur)
                cur = cur.next
            if len(st) < k:
                break
            
            cur = st[-1].next
            while st:
                node = st.pop(-1)
                prev.next = node
                prev = prev.next
            prev.next = cur
        
        return dummy.next

