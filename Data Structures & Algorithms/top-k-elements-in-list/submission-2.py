class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt = defaultdict(int)

        for num in nums:
            dt[num]+=1
        
        hp = []

        for key in dt.keys():
            heapq.heappush(hp, (dt[key], key))
            if len(hp) > k:
                heapq.heappop(hp)
            
        return [val for _, val in hp]
