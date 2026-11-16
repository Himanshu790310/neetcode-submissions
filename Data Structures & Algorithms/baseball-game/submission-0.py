from collections import deque
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        while operations:
            x = operations.pop(0)
            try:
                stack.append(int(x))
            except ValueError:
                if x == '+':
                    stack.append(stack[-1]+stack[-2])
                elif x == "C":
                    stack.pop()
                elif x == 'D':
                    stack.append(stack[-1]*2)
        return sum(stack)
