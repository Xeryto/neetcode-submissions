class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        ans = 0
        rob = [0]*len(nums)

        rob[0] = nums[0]
        rob[1] = max(rob[0], nums[1])

        for i in range(2, len(nums)-1):
            rob[i] = max(rob[i-2]+nums[i], rob[i-1])
        
        ans = rob[len(nums)-2]

        rob = [0]*len(nums)

        rob[0] = 0
        rob[1] = max(rob[0], nums[1])

        for i in range(2, len(nums)):
            rob[i] = max(rob[i-2]+nums[i], rob[i-1])
        
        ans = max(ans, rob[len(nums)-1])
        
        return ans
        