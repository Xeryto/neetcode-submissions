class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)
        while l < r:
            center = l+(r-l)//2
            if nums[center] < target:
                l+=1
            elif nums[center] > target:
                r-=1
            else:
                return center
        else:
            return -1