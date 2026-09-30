class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total %k != 0:
            return False
        
        subsets = [0]*k

        sumper = total//k

        nums.sort(reverse=True)

        def dfs(i):
            if i == len(nums):
                return len(set(subsets)) == 1
            
            for side in range(k):
                if subsets[side]+nums[i] <= sumper:
                    subsets[side]+=nums[i]
                    if dfs(i+1):
                        return True
                    subsets[side]-=nums[i]
                
                if subsets[side] == 0:
                    break
            
            return False

        return dfs(0)
            