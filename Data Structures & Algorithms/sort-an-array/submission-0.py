class Solution:
    def merge(self, left, right):
        l,r = 0,0
        result = []

        while l < len(left) and r < len(right):
            if right[r] < left[l]:
                result.append(right[r])
                r+=1
            else:
                result.append(left[l])
                l+=1
        
        if l < len(left):
            result.extend(left[l:])

        if r < len(right):
            result.extend(right[r:])
        
        return result
        
        
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        
        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left,right)