class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for string in strs:
            i = 0
            while i < min(len(common),len(string)) and string[i] == common[i]:
                i+=1
            common = common[:i]
        
        return common
