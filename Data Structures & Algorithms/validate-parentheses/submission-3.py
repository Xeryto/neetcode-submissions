class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()

        mp = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in mp.keys():
                if len(st) == 0 or st[-1] != mp[ch]:
                    return False
                st.pop()
            else:
                st.append(ch)
            
        return len(st) == 0