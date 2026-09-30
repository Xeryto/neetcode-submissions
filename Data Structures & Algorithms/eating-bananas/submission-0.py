class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        l,r = 1, max(piles)

        while l <= r:
            center = l+(r-l)//2
            print(l,r,center)

            curHours = sum([math.ceil(piles[i]/center) for i in range(len(piles))])
            print(curHours)

            if sum([math.ceil(piles[i]/center) for i in range(len(piles))]) > h:
                l = center+1
            elif sum([math.ceil(piles[i]/center) for i in range(len(piles))]) <= h:
                r = center-1
        return l