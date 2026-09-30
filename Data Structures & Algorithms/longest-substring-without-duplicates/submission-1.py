class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        ans = 0

        dt = defaultdict(int)

        l,r = 0, 0

        while r < len(s):
            while dt[s[r]] == 1:
                dt[s[l]]-=1
                l+=1
            
            dt[s[r]]+=1
            
            ans = max(ans, r-l+1)
            
            r+=1
        
        return ans