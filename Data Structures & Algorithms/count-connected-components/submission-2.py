class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self, i):
        cur, parent = i, self.parent[i]
        while cur != parent:
            cur = parent
            parent = self.parent[cur]
        
        return cur
    
    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)

        if self.rank[i] < self.rank[j]:
            i,j = j, i

        if self.parent[j] == i:
            return False
        
        self.parent[j] = i
        self.rank[i]+=self.rank[j]
        return True
    

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        ans = n
        for i,j in edges:
            if dsu.union(i,j):
                ans-=1
        
        return ans
