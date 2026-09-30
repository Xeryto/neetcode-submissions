class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []

        def dfs(index):
            if index == len(nums):
                return
            
            visited = set()

            for i in range(index, len(nums)):
                if nums[i] in visited:
                    continue
                else:
                    cur.append(nums[i])
                    visited.add(nums[i])
                    dfs(i+1)
                    ans.append(cur.copy())
                    cur.pop(-1)
            
        nums.sort()
        dfs(0)
        ans.append(cur.copy())
        return ans

            