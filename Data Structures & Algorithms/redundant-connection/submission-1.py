class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
    
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UF(n)
        count = n

        for a,b in edges:
            if not uf.union(a,b):
                return [a,b]
        print(count)
        return uf.parents
