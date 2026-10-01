class Solution:
    # runtime 128ms
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()
        for s in strs:
            t = sorted(s)
            t = "".join(t)
            res = seen.get(t,None)
            if res != None:
                res.append(s)
            else:
                seen[t] = [s]
        return list(seen.values())
