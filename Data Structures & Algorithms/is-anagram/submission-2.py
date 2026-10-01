class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_count = s.count(s[i])
            t_count = t.count(s[i])
            if s_count != t_count:
                return False
        return True 
