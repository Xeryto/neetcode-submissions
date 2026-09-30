class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        dt = {}
        cur = []
        ans = []

        for num in nums:
            dt[num] = num
        
        

        def dfs():
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return
            keys = list(dt.keys())
            for num in keys:
                cur.append(num)
                del dt[num]
                dfs()
                cur.pop()
                dt[num] = num
            
        dfs()

        return ans