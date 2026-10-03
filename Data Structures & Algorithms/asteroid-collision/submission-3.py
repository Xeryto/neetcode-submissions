class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for ast in asteroids:
            st.append(ast)
            if ast > 0:
                continue
            while len(st) > 1 and st[-1] < 0 and st[-2] > 0:
                right,left = st.pop(-1), st.pop(-1)
                if abs(right) < abs(left):
                    st.append(left)
                elif abs(right) > abs(left):
                    st.append(right)
        
        return st
