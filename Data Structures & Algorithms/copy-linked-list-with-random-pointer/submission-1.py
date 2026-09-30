"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        while cur:
            duplicate = Node(cur.val, cur.next)
            cur.next = duplicate
            cur = cur.next.next
        
        cur = head
        while cur:
            duplicate = cur.next
            if cur.random:
                duplicate.random = cur.random.next
            cur = cur.next.next
        
        cur = head.next
        while cur and cur.next:
            cur.next = cur.next.next
            cur = cur.next
        
        newhead = head.next
        head.next = None
        
        return newhead