class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*stones[i] for i in range(len(stones))]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y,x = heapq.heappop(stones), heapq.heappop(stones)
            if x != y:
                y -= x
                heapq.heappush(stones, y)
        
        return -stones[0] if stones else 0