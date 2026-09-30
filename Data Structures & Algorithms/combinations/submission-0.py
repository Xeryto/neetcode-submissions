class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        cur = []
        ans = []
        def dfs(i):
            nonlocal cur 
            if len(cur) == k:
                ans.append(cur.copy())
                return
            
            for num in range(i, n+1):
                cur.append(num)
                dfs(num+1)
                cur.pop(-1)
        
        dfs(1)

        return ans

                
