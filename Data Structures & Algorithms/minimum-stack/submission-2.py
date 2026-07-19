class MinStack:


    # [None, None, None]

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val) # O(1)
        if self.min_stk:
            if val <= self.min_stk[-1]:
                self.min_stk.append(val)
        else:
            self.min_stk.append(val)
            # in the other case, do nothing


    
    def pop(self) -> None:
        popped = self.stk.pop()
        if popped == self.min_stk[-1]:
            self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]

        
