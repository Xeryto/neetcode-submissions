class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        dt = defaultdict(int)
        for ch in t:
            dt[ch] +=1
        l,r = 0, 0
        ans = (0,0)
        anslen = float("infinity")
        while r < len(s):
            if max(list(dt.values())) > 0:
                if s[r] in dt:
                    dt[s[r]]-=1
                r+=1
            else:
                while max(list(dt.values())) <= 0 and l < r:
                    if s[l] in dt:
                        dt[s[l]]+=1
                    l+=1
                if r-l+2 < anslen:
                    anslen = r-l+2
                    ans = (l-1, r)
        
        if max(list(dt.values())) <= 0:
            while max(list(dt.values())) <= 0 and l < r:
                if s[l] in dt:
                    dt[s[l]]+=1
                l+=1
            if r-l+2 < anslen:
                ans = (l-1, r)

        return s[ans[0]:ans[1]]