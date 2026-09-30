class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt = defaultdict(int)
        for i in range(len(nums)):
            dt[nums[i]]+=1
        
        pq = []
        for key, value in dt.items():
            heapq.heappush(pq, (-value, key))
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(pq)[1])
        
        return ans