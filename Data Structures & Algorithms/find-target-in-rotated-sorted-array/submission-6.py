class Solution:
    def findMin(self, nums):
        l,r = 0, len(nums)-1

        while l < r:
            mid = l+(r-l)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        
        return l

    def search(self, nums: List[int], target: int) -> int:
        split = self.findMin(nums)

        if nums[split] <= target <= nums[-1]:
            l,r = split, len(nums)-1
        else:
            l,r = 0, split-1

        print(l,r)
        
        while l <= r:
            mid = l+(r-l)//2
            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        
        return -1
