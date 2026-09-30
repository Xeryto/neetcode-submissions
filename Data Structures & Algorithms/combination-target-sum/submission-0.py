class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []

        def dfs(index):
            for i in range(index, len(nums)):
                print(sum(cur),nums[i], target)
                if sum(cur)+nums[i] > target:
                    continue
                elif sum(cur)+nums[i] == target:
                    cur.append(nums[i])
                    ans.append(cur.copy())
                    cur.pop()
                else:
                    cur.append(nums[i])
                    dfs(i)
                    cur.pop()
        dfs(0)
        return ans