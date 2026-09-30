class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = defaultdict(list)

        for i, num in enumerate(nums):
            mp[num].append(i)

        for num in mp.keys():
            if target-num in mp:
                if target == num*2:
                    if len(mp[num]) > 1:
                        return [mp[num][0], mp[num][1]]
                    continue
                return sorted([mp[num][0], mp[target-num][0]])
        