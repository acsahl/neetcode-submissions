class MinStack:

    def __init__(self):
        self.stack = []
        self.m = None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.m is not None:
            if val < self.m:
                self.m = val
        else:
            self.m = val
        

    def pop(self) -> None:
        self.stack.pop(-1)
        if self.stack:
            self.m = min(self.stack)
        else:
            self.m = None

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.m
        
