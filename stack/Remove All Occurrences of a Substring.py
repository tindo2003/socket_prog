class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= len(part):
                r1, r2 = len(stack) - 1, len(part) - 1
                removable = True
                while r2 >= 0:
                    if stack[r1] != part[r2]:
                        removable = False
                        break
                    r1 -= 1
                    r2 -= 1
                if removable:
                    for _ in range(len(part)):
                        stack.pop()
        return "".join(stack)
