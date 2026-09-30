class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        while l < r:
            mid = l+(r-l)//2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid+1
            
        return r

    def search(self, nums: List[int], target: int) -> int:
        split = self.findMin(nums)
        if target < nums[split]:
            return -1

        if target <= nums[-1]:
            l,r = split, len(nums)-1
        else: 
            l, r = 0, split-1

        while l <= r:
            mid = l+(r-l)//2
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                return mid
        return -1
                