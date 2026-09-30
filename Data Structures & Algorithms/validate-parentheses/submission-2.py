class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()

        closing = {')': '(', ']': '[', '}': '{'}
        
        for ch in s:
            if ch in closing:
                if len(st) == 0 or st[-1] != closing[ch]:
                    return False
                st.pop()
            
            else: st.append(ch)
        
        return len(st) == 0
