class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        curMax = 0
        while l < r:
            if height[r] >= height[l]:
                curMax = max(curMax, (r-l)*height[l])
                l+=1
            else:
                curMax = max(curMax, (r-l)*height[r])
                r-=1
            
        
        return curMax