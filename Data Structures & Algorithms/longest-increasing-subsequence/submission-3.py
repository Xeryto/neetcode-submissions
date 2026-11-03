class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]

        for i, num in enumerate(nums):
            if i == 0:
                continue
            mx = 0

            for j in range(i):
                if nums[j] < nums[i]:
                    mx = max(mx, dp[j])
            
            dp[i] = mx+1
        
        return max(dp)