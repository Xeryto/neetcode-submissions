class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        postf = [1]

        n = len(nums)

        for i in range(n):
            pref.append(nums[i]*pref[-1])
            postf = [nums[n-i-1]*postf[0]]+postf

        output = []
        for i in range(n):
            output.append(pref[i]*postf[i+1])

        print(pref, postf)
        
        return output