class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if len(matchsticks) < 4 or total%4 != 0:
            return False

        length = total//4

        n = len(matchsticks)
        
        sides = [0]*4

        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == n:
                return (sides[0]==sides[1]==sides[2]==sides[3])

            for side in range(4):
                if sides[side]+matchsticks[i] <= length:
                    sides[side]+=matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[side]-=matchsticks[i]
                
                if sides[side]==0:
                    break

            return False
        
        return dfs(0)