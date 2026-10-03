class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            l,r = 0, len(nums)-1

            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
        
        return nums