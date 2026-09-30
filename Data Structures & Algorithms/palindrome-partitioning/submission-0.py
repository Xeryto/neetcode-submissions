class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cur = []
        ans = []
        frm = 0

        print(s, s[2:-1:-1])

        def dfs(i):
            nonlocal frm


            if i == len(s)-1:
                if s[frm:i+1] == s[i:frm-1:-1] or (frm == 0 and s[frm:i+1] == s[i::-1]):
                    cur.append(s[frm:i+1])
                    ans.append(cur.copy())
                    cur.pop(-1)
                return
            
            # print(frm, i, s[frm:i+1], s[i:frm-1:-1], s[i::-1], s[frm:i+1] == s[i:frm-1:-1] or (frm == 0 and s[frm:i+1] == s[i::-1]))
            if s[frm:i+1] == s[i:frm-1:-1] or (frm == 0 and s[frm:i+1] == s[i::-1]):
                cur.append(s[frm:i+1])
                temp, frm = frm, i+1
                dfs(i+1)
                frm = temp
                cur.pop(-1)
            
            dfs(i+1)

        dfs(0)
        return ans
            

