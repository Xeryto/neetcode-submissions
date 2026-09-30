class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for st in strs:
            ans+=str(len(st))+"#"+st
        
        return ans

    def decode(self, s: str) -> List[str]:
        print(s)
        curNum = ""
        ans = []
        skip = 0
        for i in range(len(s)):
            if skip:
                skip-=1
                continue
            if s[i] in "0123456789":
                curNum+=s[i]
            elif s[i] == "#":
                curNum = int(curNum)
                ans.append(s[i+1:i+1+curNum])
                skip = curNum
                curNum = ""
        
        return ans
