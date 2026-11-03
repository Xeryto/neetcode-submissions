class Solution:
    def checkValidString(self, s: str) -> bool:
        if s[0] == ')' or s[-1] == '(':
            return False

        st_p, st_s = [], []

        for i, ch in enumerate(s):
            if ch == '(':
                st_p.append(i)
            elif ch == '*':
                st_s.append(i)
            else:
                if len(st_p) != 0:
                    st_p.pop(-1)
                elif len(st_s) != 0:
                    st_s.pop(-1)
                else:
                    return False
        
        while st_p and st_s:
            idx = st_p[-1]

            if st_s[-1] < idx:
                return False
            
            st_s.pop(-1)
            st_p.pop(-1)
        
        return not st_p
