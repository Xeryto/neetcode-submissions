class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        if nums[0] > nums[-1]:
            sl, sr = 0, len(nums)-1
            while sl < sr:
                mid = sl+(sr-sl)//2
                print(sl,sr,mid)

                if nums[mid] > nums[sr]:
                    sl = mid+1
                else:
                    sr = mid
                    
            if target <= nums[-1]:
                l = sl
            else:
                r = sl-1
        print(l,r)
        while l <= r:
            mid = l+(r-l)//2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        
        return -1

        


