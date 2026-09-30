class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, j):
            if i >= len(nums):
                return 0
            
            ans = 0
            if j == -1 or nums[i] > nums[j]:
                ans = 1+memo.get((i+1, i), dfs(i+1, i))
            
            return max(ans, memo.get((i+1, j), dfs(i+1, j)))

        return dfs(0, -1)
