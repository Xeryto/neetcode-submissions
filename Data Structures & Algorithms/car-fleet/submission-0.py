class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(position[i], speed[i]) for i in range(len(position))], key=lambda x: -x[0])

        stack = []

        stack.append((target-cars[0][0])/cars[0][1])
        fleets = 1

        for pos, spd in cars:
            if (target-pos)/spd <= stack[-1]:
              continue  
            else:
                fleets+=1
                stack.append((target-pos)/spd)
            
        return fleets