class Solution:
    def helper(self, op, closed, n, base):
        ans = []
        if op+closed == 2*n:
            return [base]
        if op<n:
            ans.extend(self.helper(op+1, closed, n, base+"("))
        if closed<n and closed < op:
            ans.extend(self.helper(op, closed+1, n, base+")"))
        return ans

    def generateParenthesis(self, n: int) -> List[str]:
        return self.helper(1, 0, n, "(")