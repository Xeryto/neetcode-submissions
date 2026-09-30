class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [-stone for stone in stones]
        heapq.heapify(hp)

        while len(hp) > 1:
            x,y = heapq.heappop(hp), heapq.heappop(hp)

            if x == y:
                continue
            
            if x < y:
                x,y = y,x

            heapq.heappush(hp, y-x)

        return -hp[0] if len(hp) > 0 else 0