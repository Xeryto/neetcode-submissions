class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0, 0
        dt = defaultdict(int)
        maxf = 0
        ans = 0
        while r < len(s):
            dt[s[r]] += 1
            maxf = max(maxf, dt[s[r]])

            while (r-l+1) - maxf > k:
                dt[s[l]]-=1
                l+=1
            
            ans = max(ans, r-l+1)
            
            r+=1
        
        return ans
        
        return max(ans, r-l)
                
                    

