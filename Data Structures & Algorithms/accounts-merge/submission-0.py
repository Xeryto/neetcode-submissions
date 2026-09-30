class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
        
    
    def find(self, cur):
        while self.parent[cur] != cur:
            cur = self.parent[cur]
        
        return cur
    
    def union(self, a,b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False

        if self.rank[a] < self.rank[b]:
            a,b = b,a

        self.parent[b] = a
        self.rank[a]+=self.rank[b]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        emailToAcc = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    dsu.union(emailToAcc[email], i)
                else:
                    emailToAcc[email] = i
        
        emailGroup = defaultdict(list)

        for email, index in emailToAcc.items():
            leader = dsu.find(index)
            emailGroup[leader].append(email)
        
        res = []

        for index in emailGroup.keys():
            name = accounts[index][0]
            res.append([name]+sorted(emailGroup[index]))

        return res
            