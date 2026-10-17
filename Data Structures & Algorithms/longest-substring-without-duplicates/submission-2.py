class Solution:
    def lengthOfLongestSubstring(self,s : str)->int:
        if not s:
            return 0
        if len(s)==1:
            return 1
        seen = set()
        left,right = 0,0
        max_l = 0
        while right<len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            right+=1
            if len(seen)>max_l:
                max_l = len(seen)
        return max_l