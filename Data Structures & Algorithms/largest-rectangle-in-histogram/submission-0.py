class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [0]

        area = [0]*len(heights)

        for i in range(1,len(heights)):
            while st and heights[i] < heights[st[-1]]:
                cur = st.pop(-1)
                area[cur] += heights[cur]*(i-cur)
            st.append(i)

        while st:
            cur = st.pop(-1)
            area[cur] += heights[cur]*(len(heights)-cur)
        
        st = [len(heights)-1]

        for i in range(len(heights)-2, -1, -1):
            while st and heights[i] < heights[st[-1]]:
                cur = st.pop(-1)
                area[cur] += heights[cur]*(cur-i-1)
            st.append(i)
        
        st.pop(-1)
        
        while st:
            cur = st.pop(-1)
            area[cur] += heights[cur]*(cur)
        
        return max(area)