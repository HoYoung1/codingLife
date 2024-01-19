import sys


class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = sys.maxsize

    def push(self, val: int) -> None:
        if self.current_min > val:
            self.current_min = val
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.current_min:
            self.current_min = min(self.stack[:-1])
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.current_min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()