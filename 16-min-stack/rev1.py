class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


stack = MinStack()
stack.push(1)
stack.push(2)
stack.push(0)
print(stack.getMin())
stack.pop()
print(stack.top())
print(stack.getMin())