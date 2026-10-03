class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for op in operations:
            if op == "C":
                st.pop(-1)
                continue
            if op == "D":
                st.append(st[-1]*2)
                continue
            if op == "+":
                st.append(st[-1]+st[-2])
                continue
            
            st.append(int(op))
        
        return sum(st)
            
