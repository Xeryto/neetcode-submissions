class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos, neg, ans = 1, 1, -float("inf")

        for i in range(len(nums)):
            pos, neg = max(nums[i], pos*nums[i], neg*nums[i]), min(nums[i], pos*nums[i], neg*nums[i])
            ans = max(ans, pos)
        
        return ans

            