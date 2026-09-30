class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = defaultdict(int)
        pref[0] = 1

        curTotal = 0
        ans = 0
        for i in range(len(nums)):
            curTotal+=nums[i]
            ans += pref[curTotal-k]
            pref[curTotal]+=1
        
        return ans