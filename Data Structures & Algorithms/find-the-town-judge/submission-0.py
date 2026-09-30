class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        trusts = {i+1: 0 for i in range(n)}
        trusted = {i+1: 0 for i in range(n)}

        a,b = set(), set(i+1 for i in range(n))

        for i,j in trust:
            trusted[j] +=1
            trusts[i] +=1
            if i in b:
                b.remove(i)
            if trusted[j] == n-1:
                a.add(j)
        
        return a.intersection(b).pop() if a.intersection(b) else -1