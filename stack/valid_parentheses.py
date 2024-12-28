class Solution:
    def isValid(self, s: str) -> bool:
        lst = list(s)
        m = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in lst:
            if c in [")", "]", "}"]:
                if not stack:
                    return False
                if stack[-1] != m[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0
