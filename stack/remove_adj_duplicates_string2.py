class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for item in s:
            if stack:
                top = stack[-1]
                if item == top[0]:
                    top[1] += 1
                    if top[1] == k: 
                        stack.pop()
                    continue
            stack.append([item, 1])
        tmp = []
        for item, freq in stack:
            tmp.append(item * freq)
        
        return "".join(tmp)