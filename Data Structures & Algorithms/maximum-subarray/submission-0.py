class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        ans = -float('inf')

        for i in range(len(nums)):
            curSum = max(curSum+nums[i], nums[i])
            ans = max(ans, curSum)
        
        return ans