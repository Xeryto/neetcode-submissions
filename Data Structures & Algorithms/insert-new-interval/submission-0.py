class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i+=1
        
        if i == len(intervals):
            intervals.append(newInterval)
            return intervals
        
        if i == 0 and intervals[0][0] > newInterval[1]:
            return [newInterval]+intervals
        
        j = len(intervals)-1
        while j > i and newInterval[1] < intervals[j][0]:
            j-=1
        
        if j == i and intervals[i-1][1] < newInterval[0] and intervals[i][0] > newInterval[1]:
            return intervals[:j]+[newInterval]+intervals[j:]
        
        mn = min(intervals[i][0], newInterval[0])

        while i != j:
            del intervals[j-1]
            j-=1
        
        intervals[i][0] = mn
        intervals[i][1] = max(intervals[i][1], newInterval[1])

        return intervals
