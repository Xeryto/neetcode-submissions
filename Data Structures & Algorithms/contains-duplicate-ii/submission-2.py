class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        mp = defaultdict(int)
        for i in range(min(len(nums), k+1)):
            mp[nums[i]]+=1
            if mp[nums[i]] > 1:
                return True
        if len(mp) < k+1:
            return False
        
        
        l,r = 0, k+1
        while r < len(nums):
            mp[nums[l]]-=1
            mp[nums[r]]+=1
            if mp[nums[r]] > 1:
                return True
            l+=1
            r+=1
        
        return False
