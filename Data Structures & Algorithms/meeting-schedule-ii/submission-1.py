"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([intervals[i].start for i in range(len(intervals))])
        ends = sorted([intervals[i].end for i in range(len(intervals))])
        
        ans = 0
        cur = 0
        l,r = 0,0

        print(starts,ends)

        while l < len(intervals):
            if starts[l] < ends[r]:
                cur+=1
                l+=1
            else:
                ans = max(ans, cur)
                cur-=1
                r+=1
        
        return max(ans,cur)