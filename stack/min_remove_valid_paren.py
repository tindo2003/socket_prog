

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        N = len(s)
        for idx in range(N):
            c = s[idx]
            if c == ")":
                if not stack or stack[-1][0] != "(":
                    continue
                else:
                    stack.pop()
            else:
                if c == "(":
                    stack.append((c, idx))
        
        stack1 = []
        for idx in range(N-1, -1, -1):
            c = s[idx]
            if c == "(":
                if not stack1 or stack1[-1][0] != ")":
                    continue
                else:
                    stack1.pop()
            else:
                if c == ")":
                    stack1.append((c, idx))
        
        idx_to_remove = set([item[1] for item in stack1] + [item[1] for item in stack])

        res = []
        for idx, c in enumerate(s):
            if idx not in idx_to_remove:
                res.append(c)
        
        return "".join(res)