class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
    
    def find(self, node):
        if self.parents[node] == node:
            return node
        return self.find(self.parents[node])
    
    def union(self, a,b):
        a,b = self.find(a), self.find(b)
        if a == b:
            return False

        self.parents[b] = a
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        count = n

        for a,b in edges:
            if uf.union(a,b):
                count-=1
            
        return count
