class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        cur = ""
        ans = []

        def dfs(i):
            nonlocal cur
            if i >= len(digits):
                ans.append(cur)
                return
            
            for letter in mapping[digits[i]]:
                cur+=letter
                dfs(i+1)
                cur = cur[:len(cur)-1]
        
        if not digits:
            return []
        dfs(0)
        return ans
