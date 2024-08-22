class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack:
                top = stack[-1]
                if c == top:
                    stack.pop()
                    continue
            stack.append(c)
        return "".join(stack)