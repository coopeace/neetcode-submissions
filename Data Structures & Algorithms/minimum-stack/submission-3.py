class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins)!=0 :
            self.mins.append(min(val,self.mins[-1]))
        else:
            self.mins.append(val)

    def pop(self) -> None:
        if len(self.stack)!=0:
            self.stack.pop()
            self.mins.pop()

    def top(self) -> int:
        return None if len(self.stack)==0 else self.stack[-1]
        
    def getMin(self) -> int:
        return None if len(self.mins)==0 else self.mins[-1]
