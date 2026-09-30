from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(sqrt(pow(points[i][0], 2)+pow(points[i][1], 2)), points[i]) for i in range (len(points))]

        heapq.heapify(heap)
        
        ans = [heapq.heappop(heap)[1] for _ in range (k)]

        return ans