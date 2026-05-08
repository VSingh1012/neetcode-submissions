class MinStack:

    def __init__(self):
        self.CURR_MAX = 50
        self.stk = [None] * self.CURR_MAX
        self.end_ptr = 0
        

    def push(self, val: int) -> None:
        self.stk[self.end_ptr] = val
        self.end_ptr += 1

    def pop(self) -> None:
        if self.stk:
            curr_last = self.stk[self.end_ptr - 1]
            self.end_ptr -= 1
        else:
            curr_last = None

    def top(self) -> int:
        
        return self.stk[self.end_ptr - 1]
        

    def getMin(self) -> int:
        sample_stk = sorted(self.stk[0:self.end_ptr])
        return sample_stk[0]
        