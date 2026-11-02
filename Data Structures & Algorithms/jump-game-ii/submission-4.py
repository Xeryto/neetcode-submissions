class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        count = 0

        if len(nums) == 1:
            return 0

        while i+nums[i] < len(nums)-1:
            print(i)
            j = nums[i]
            max_add = 0
            new_i = 0
            for k in range(i+1, i+j+1):
                if k >= len(nums):
                    break
                if k+nums[k] >= max_add:
                    max_add = max(max_add, k+nums[k])
                    new_i = k

            i=new_i
            count+=1
        
        return count+1