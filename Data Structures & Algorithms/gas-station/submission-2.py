class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        
        tank = 0
        index = 0

        i = 0

        while not(i%n == index and i!=index):
            tank+=gas[i%n]-cost[i%n]
            i+=1
            if tank < 0:
                tank = 0
                index = (i)%n
            
            
        return index