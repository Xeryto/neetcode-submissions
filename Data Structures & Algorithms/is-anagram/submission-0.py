class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dt = defaultdict(int)
        for ch in s:
            dt[ch]+=1
        for ch in t:
            if ch not in dt:
                return False
            dt[ch]-=1
            if dt[ch] == 0:
                del dt[ch]
        return len(dt) == 0