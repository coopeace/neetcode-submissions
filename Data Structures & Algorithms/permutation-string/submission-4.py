class Solution:
    def checkInclusion(self,s1:str,s2:str)->bool:
        if len(s1)>len(s2): return False
        key1 = [0]*26
        key2 = [0]*26
        for char in s1:
            key1[ord(char)-ord('a')]+=1
        left = 0
        for right in range(len(s2)):
            key2[ord(s2[right])-ord('a')]+=1
            if right - left + 1 == len(s1):
                if key1 == key2 :
                    return True
                else :
                    key2[ord(s2[left])-ord('a')]-=1
                    left+=1
        return False