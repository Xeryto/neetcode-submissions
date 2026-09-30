class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = [-num for num in nums]
        heapq.heapify(ans)

        for i in range(k-1):
            heapq.heappop(ans)
        
        return -heapq.heappop(ans)