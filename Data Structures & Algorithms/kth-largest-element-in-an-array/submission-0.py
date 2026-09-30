class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [nums[i]*(-1) for i in range(len(nums))]
        heapq.heapify(nums)

        for i in range(k):
            ans = heapq.heappop(nums)
        
        return -1*ans
