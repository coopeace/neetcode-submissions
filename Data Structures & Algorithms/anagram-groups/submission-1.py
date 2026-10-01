class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            t = sorted(s)
            t = "".join(t)
            if t in seen:
                value = seen[t]
                value.append(s)
                seen[t] = value
            else:
                temp = []
                temp.append(s)
                seen[t] = temp
        return list(seen.values())
