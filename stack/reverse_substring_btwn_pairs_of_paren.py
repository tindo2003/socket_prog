class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ")":
                tmp = ""
                while stack[-1] != "(":
                    ele = stack.pop()
                    tmp += ele 
                stack.pop()
                for c in tmp:
                    stack.append(c)
            else:
                stack.append(c)
        return "".join(stack)
        
