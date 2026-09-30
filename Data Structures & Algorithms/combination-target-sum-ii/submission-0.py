class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cur = []
        ans = []

        candidates.sort()

        def dfs(i):
            if sum(cur) == target:
                ans.append(cur.copy())
                return
            
            if sum(cur) > target or i >= len(candidates):
                return
            
            el = candidates[i]
            cur.append(el)
            dfs(i+1)
            cur.pop()
            while i < len(candidates)-1 and el == candidates[i+1]:
                i+=1
            dfs(i+1)
        
        dfs(0)
        return ans
            
