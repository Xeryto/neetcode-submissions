class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found1,found2,found3 = False, False, False

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                if triplet[0] == target[0]:
                    found1 = True
                if triplet[1] == target[1]:
                    found2 = True
                if triplet[2] == target[2]:
                    found3 = True

            
        return found1 and found2 and found3