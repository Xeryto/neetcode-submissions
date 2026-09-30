class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt = {}
        for st in strs:
            srtd = str(sorted(st))
            if srtd in dt:
                dt[srtd].append(st)
            else:
                dt[srtd] = [st]
        answr = []
        for key in dt.keys():
            answr.append(dt[key])

        return answr