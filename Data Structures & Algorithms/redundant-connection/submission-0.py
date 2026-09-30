class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        return

    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        
        return i

    def union(self, i, j):
        i,j = self.find(i), self.find(j)

        self.parent[i] = j

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for i,j in edges:
            n = max(n,i,j)
        uf = UF(n)
        
        for i,j in edges:
            i,j = i-1, j-1

            if uf.find(i) == uf.find(j):
                return [i+1,j+1]
            
            uf.union(i,j)
    
