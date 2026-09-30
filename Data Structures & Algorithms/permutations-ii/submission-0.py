class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        skipped = set()
        n = len(nums)
        cur = []
        ans = []
        nums.sort()
        def dfs():
            if len(cur) == n:
                ans.append(cur.copy())
                return
            
            for i in range(n):
                if i in skipped or (i > 0 and nums[i] == nums[i-1] and i-1 not in skipped):
                    continue
                skipped.add(i)
                cur.append(nums[i])
                dfs()
                skipped.remove(i)
                cur.pop(-1)
        
        dfs()

        return ans
