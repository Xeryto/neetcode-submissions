"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def recurse(n, xfrom, yfrom):
            match = grid[yfrom][xfrom]
            split = False
            for i in range(yfrom, yfrom+n):
                for j in range(xfrom, xfrom+n):
                    if grid[i][j] != match:
                        split = True
                        break
            if not(split):
                leaf = Node(grid[yfrom][xfrom], isLeaf = True)
                return leaf
            node = Node()
            node.topLeft = recurse(n//2, xfrom, yfrom)
            node.topRight = recurse(n//2, xfrom+n//2, yfrom)
            node.bottomLeft = recurse(n//2, xfrom, yfrom+n//2)
            node.bottomRight = recurse(n//2, xfrom+n//2, yfrom+n//2)
            return node


        
        n = len(grid)
        return recurse(n, 0,0)