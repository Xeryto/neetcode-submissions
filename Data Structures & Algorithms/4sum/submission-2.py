class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []

        for i,num in enumerate(nums):
            if num > target and num >= 0:
                break
            if num == nums[i-1] and i!=0:
                continue
            for j,nm in enumerate(nums[i+1:]):
                if num+nm > target and num+nm >= 0:
                    break
                
                if nm == nums[i+1+j-1] and j!=0:
                    continue
                
                l,r = i+1+j+1, len(nums)-1
                print(i,j,l,r)
                while l < r:
                    sm = num+nm+nums[l]+nums[r]

                    if sm < target:
                        l+=1
                    elif sm > target:
                        r-=1
                    else:
                        res.append([num,nm,nums[l], nums[r]])
                        l+=1
                        r-=1
                        while nums[l] == nums[l-1] and l < r:
                            l+=1
                            continue
        
        return res