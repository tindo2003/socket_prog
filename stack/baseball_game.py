from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                top = stack[-1]
                stack.append(2 * top)
            elif op == "+":
                n1 = stack[-1]
                n2 = stack[-2]
                stack.append(n1 + n2)
            else:
                stack.append(int(op))

        return sum(stack)
