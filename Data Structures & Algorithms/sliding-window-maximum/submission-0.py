class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        ans = []

        for i in range(k-1):
            heapq.heappush(heap, (-nums[i], i))

        l,r = 0, k-1
        while r < len(nums):
            heapq.heappush(heap, (-nums[r], r))

            while heap and not (l <= heap[0][1] <= r):
                heapq.heappop(heap)
            
            ans.append(-heap[0][0])

            l+=1
            r+=1
        
        return ans
                
                

