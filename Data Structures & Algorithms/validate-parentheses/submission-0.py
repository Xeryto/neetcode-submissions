class Solution:
    def isValid(self, s: str) -> bool:
        dt = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for ch in s:
            if ch in dt.values():
                stack.append(ch)
            else:
                if len(stack) == 0 or stack[-1] != dt[ch]:
                    return False
                stack.pop(-1)
        
        return len(stack) == 0