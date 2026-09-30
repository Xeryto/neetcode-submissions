class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        dt = defaultdict(int)

        for ch in s1:
            dt[ch]+=1
        
        n = len(s1)

        for i in range(n):
            if s2[i] in dt:
                dt[s2[i]]-=1
        
        if len(set(dt.values())) == 1 and list(dt.values())[0] == 0:
            return True

        for i in range(n, len(s2)):
            if s2[i-n] in dt:
                dt[s2[i-n]]+=1
            if s2[i] in dt:
                dt[s2[i]]-=1
            if len(set(dt.values())) == 1 and list(dt.values())[0] == 0:
                return True
        
        return False