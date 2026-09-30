class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        if len(intervals) == 1:
            return intervals
        heapq.heapify(intervals)
        prev = heapq.heappop(intervals)
        ans.append(prev)
        while intervals:
            cur = heapq.heappop(intervals)
            if cur[0] <= prev[1]:
                prev[1] = max(prev[1], cur[1])
                ans[-1][1] = prev[1]
            else:
                ans.append(cur)
                prev = cur
        
        return ans
