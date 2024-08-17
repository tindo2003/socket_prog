

class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = []
        for c in s:
            if c == ")":
                stack.pop()
            elif c == "(":
                stack.append("(")
            ans = max(ans, len(stack))
        return ans

def main():
    sol = Solution()
    s = "(1+(2*3)+((8)/4))+1"
    res = sol.maxDepth(s)
    print(res)

if __name__ == "__main__":
    main()