class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=list()
        first=False
        for ch in tokens:
            match ch :
                case "+" :
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(x+y)
                case "-" :
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(x-y)
                case "*" :
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(x*y)
                case "/" :
                    y = stack.pop()
                    x = stack.pop()
                    stack.append(int(x/y))
                case _ :
                    stack.append(int(ch))
        return stack[0]
