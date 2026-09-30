class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        half = len(nums1)+(len(nums2)-len(nums1))//2

        l,r = 0, len(nums1)-1
        while True:
            mid = l+(r-l)//2
            j = half-mid-2

            Aleft = nums1[mid] if mid >=0 else float("-infinity")
            Aright = nums1[mid+1] if (mid+1) < len(nums1) else float("infinity")

            Bleft = nums2[j] if j >=0 else float("-infinity")
            Bright = nums2[j+1] if (j+1) < len(nums2) else float("infinity")
        
            if Aleft <= Bright and Bleft <= Aright:
                if (len(nums1)+len(nums2))%2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = mid - 1
            else:
                l = mid + 1



