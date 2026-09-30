"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        def bfs(node):
            q = deque([node])
            newnode = Node(node.val)
            head = newnode
            visited = {node.val: newnode}

            while q:
                cur = q.popleft()
                parent = visited[cur.val]
                for neighbor in cur.neighbors:
                    if neighbor.val in visited:
                        parent.neighbors.append(visited[neighbor.val])
                        continue
                    q.append(neighbor)
                    newnode = Node(neighbor.val)
                    parent.neighbors.append(newnode)
                    visited[neighbor.val] = newnode
                
            return head
        
        return bfs(node)
