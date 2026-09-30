class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        ans = [0]*len(temperatures)
        for i in range(1, len(temperatures)):
            temp = []
            while stack and temperatures[i] > stack[-1][0]:
                el = stack.pop(-1)
                ans[el[1]]=i-el[1]           
            stack.append((temperatures[i], i))
        
        return ans