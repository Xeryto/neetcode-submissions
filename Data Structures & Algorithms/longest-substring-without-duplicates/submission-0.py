class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 3:
            return len(set(s))

        l,r = 0, 1
        st = set(s[0])
        ans = 0
        while r < len(s):
            if s[r] in st:
                ans = max(ans, r-l)
                while s[r] in st:
                    st.remove(s[l])
                    l+=1
            st.add(s[r])
            r+=1
        
        return max(ans, r-l)

