class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()

        ans,l,r = 0,0,0

        while r < len(s):
            while s[r] in sset:
                sset.remove(s[l])
                l+=1
            sset.add(s[r])
            r+=1
            ans = max(ans, r-l)
        
        return ans

        