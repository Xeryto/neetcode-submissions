class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        prevEnd = intervals[0][1]
        ans = 0
        # dp = [1]*len(intervals)

        for i in range(1,len(intervals)):
            if prevEnd > intervals[i][0]:
                ans+=1
                prevEnd = min(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]
            # for j in range(i):
            #     if intervals[j][1] <= intervals[i][0]:
            #         dp[i] = max(dp[i], 1+dp[j])
        return ans