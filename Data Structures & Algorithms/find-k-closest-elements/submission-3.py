class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = k-1
        for r in range(k, len(arr)):
            if abs(arr[ans-k+1]-x) > abs(arr[r]-x):
                ans = r
            elif abs(arr[ans-k+1]-x) < abs(arr[r]-x):
                break
        
        return arr[ans-k+1:ans+1]

