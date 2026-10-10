class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for ch in s:
            if ch.isalnum():
                ns += ch.lower()
        left = 0
        right = len(ns)-1

        while left < right:
            if ns[left] != ns[right]:
                return False
            left+=1
            right-=1
        return True

