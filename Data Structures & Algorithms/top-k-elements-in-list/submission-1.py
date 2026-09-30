class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minheap = defaultdict(int)

        for num in nums:
            minheap[num]+=1
        
        ans = sorted(minheap.keys(), key=lambda x: -minheap[x])

        return ans[:k]
        