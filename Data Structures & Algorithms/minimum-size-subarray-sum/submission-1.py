class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        sm = 0
        ans = len(nums)+1

        for r in range(len(nums)):
            sm+=nums[r]
            while sm >= target and l <= r:
                ans = min(ans, r-l+1)
                sm-=nums[l]
                l+=1
        
        return ans if ans < len(nums)+1 else 0