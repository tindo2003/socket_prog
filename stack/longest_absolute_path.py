class Solution:
    def lengthLongestPath(self, input: str) -> int:
        ans = 0
        stack_like = {-1: 0}
        tmp = input.split("\n")
        for item in tmp:
            num_tabs = item.count("\t")
            n = len(item) 
            stack_like[num_tabs] = n + stack_like[num_tabs - 1] - num_tabs
            #signify a file
            if item.count("."):
                # adding to simulate the '/'
                ans = max(ans, stack_like[num_tabs] + num_tabs)
        return ans