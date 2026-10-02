class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = {0:'(',1:'[',2:'{'}
        closed_brackets = {')':0,']':1,'}':2}
        n = len(s)
        stack = list()
        if n%2!=0:
            return False
        for ch in s:
            if ch in open_brackets.values():
                stack.append(ch)
            elif len(stack)== 0:
                return False
            else:
                index = closed_brackets[ch]
                if stack[-1] != open_brackets[index]:
                    return False
                stack.pop()
        if len(stack)!=0:
            return False

        return True


        