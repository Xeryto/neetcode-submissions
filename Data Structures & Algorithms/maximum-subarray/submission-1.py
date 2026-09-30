class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]

        dp = [-1001]*len(nums)

        dp[0] = nums[0]

        for i in range(1,len(nums)):
            dp[i] = nums[i]+max(dp[i-1], 0)
            ans = max(ans, dp[i])
        
        return ans

        
