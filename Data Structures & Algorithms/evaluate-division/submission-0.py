class DSU:
    def __init__(self):
        self.parent = {}
        self.weight = {}
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1.0

    def find(self, x):
        if x != self.parent[x]:
            orig = self.parent[x]
            self.parent[x] = self.find(orig)
            self.weight[x] *= self.weight[orig]
        return self.parent[x]

    def union(self, x,y, value):
        self.add(x)
        self.add(y)
        rootx, rooty = self.find(x), self.find(y)

        if rootx != rooty:
            self.parent[rootx] = rooty
            self.weight[rootx] = value * self.weight[y] / self.weight[x]
    
    def getratio(self,x,y):
        if x not in self.parent or y not in self.parent or self.find(x) != self.find(y):
            return -1
        
        return self.weight[x]/self.weight[y]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dsu = DSU()
        for i,eq in enumerate(equations):
            x,y = eq[0], eq[1]
            val = values[i]

            dsu.union(x,y,val)

        ans = []
        for x,y in queries:
            ans.append(dsu.getratio(x,y))
        
        print(dsu.parent)
        return ans
        