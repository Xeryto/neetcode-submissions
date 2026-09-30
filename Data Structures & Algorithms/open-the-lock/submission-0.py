class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        q = deque([("0000", 0)])

        visited = set("0000")

        while q:
            cur, level = q.popleft()
            if cur == target:
                return level
            children = []
            for i in range(4):
                repl1, repl2 = int(cur[i])-1, int(cur[i])+1
                if repl1 < 0:
                    repl1+=10
                if repl2 > 9:
                    repl2-=10
                if cur[:i]+str(repl1)+cur[i+1:] not in visited and cur[:i]+str(repl1)+cur[i+1:] not in deadends:
                    q.append((cur[:i]+str(repl1)+cur[i+1:], level+1))
                    visited.add(cur[:i]+str(repl1)+cur[i+1:])
                if cur[:i]+str(repl2)+cur[i+1:] not in visited and cur[:i]+str(repl2)+cur[i+1:] not in deadends:
                    q.append((cur[:i]+str(repl2)+cur[i+1:], level+1))
                    visited.add(cur[:i]+str(repl2)+cur[i+1:])
        return -1
                

    

