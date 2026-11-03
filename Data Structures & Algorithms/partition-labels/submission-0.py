class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        st = set(s)
        mp = {}
        
        for ch in st:
            mp[ch] = s.count(ch)
        
        cur = defaultdict(int)

        out = []

        for i in range(len(s)):
            cur[s[i]]+=1
            for ch, count in cur.items():
                if count != mp[ch]:
                    break
            else:
                out.append(sum(cur.values()))
                cur = defaultdict(int)
            

        return out
