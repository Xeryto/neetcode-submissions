class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap):
            days = 0
            remaining = cap
            for weight in weights:
                if weight > remaining:
                    days+=1
                    remaining = cap-weight
                else:
                    remaining-= weight
            days+=1
        
            return days

        l,r = max(weights), sum(weights)

        while l < r:
            mid = l+(r-l)//2
            days_cap = can_ship(mid)

            if days_cap <= days:
                r = mid
            else:
                l = mid+1
        
        return l