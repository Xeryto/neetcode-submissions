class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                curNum = num+1
                while curNum in nums:
                    curNum+=1
                if curNum-num > ans:
                    ans = curNum-num
        
        return ans