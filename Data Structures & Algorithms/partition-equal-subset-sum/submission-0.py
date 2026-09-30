class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm =  sum(nums)
        if sm %2 == 1:
            return False

        dp = [[-1]*((sm//2)+1) for i in range (len(nums)+1)]
        def dfs(i, curSum):
            if curSum == sm//2:
                return True
            if i >= len(nums) or curSum > sm//2:
                return False
            curSum+=nums[i]
            if curSum <= sm//2:
                if dp[i+1][curSum] == -1:
                    dp[i+1][curSum] = dfs(i+1, curSum)
                if dp[i+1][curSum] == True:
                    return True
            curSum-=nums[i]
            if dp[i+1][curSum] == -1:
                dp[i+1][curSum] = dfs(i+1, curSum)
            
            return dp[i+1][curSum]
        
        res = dfs(0, 0)
        return res

        # take or dont take
        # if > half then kill