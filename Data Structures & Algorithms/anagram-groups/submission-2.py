class Solution:
    # runtime 128ms
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
                seen[t] = [s]
        return list(seen.values())
