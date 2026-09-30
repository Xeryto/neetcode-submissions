class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = deque()
        
        ans = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while len(st) != 0 and temperatures[i] > temperatures[st[-1]]:
                ins = st.pop()
                ans[ins] = i-ins
            st.append(i)

        return ans            