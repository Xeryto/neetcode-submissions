class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        cur = 0
        n = len(nums)

        def dfs(i):
            nonlocal ans
            nonlocal cur
            for j in range(i, n):
                cur=cur^nums[j]
                dfs(j+1)
                ans+=cur
                cur = cur^nums[j]
        
        dfs(0)
        return ans