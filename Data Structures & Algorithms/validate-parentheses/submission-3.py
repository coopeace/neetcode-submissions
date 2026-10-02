class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        brackets = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
        }
        stack = list()
        for ch in s:
            if ch in brackets:
                stack.append(ch)
            elif len(stack) == 0:
                return False
            else:
                if ch != brackets[stack[-1]]:
                    return False
                stack.pop()

        return len(stack)==0
