class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # the trick is here to keep the maximum has seen so far on the stack.
        # so if current ele is greater than top of stack, we know it is safe to append on top of the stack
        # motonic increasing stack
        stack = [] 
        N = len(arr)
        for idx in range(N):
            # keep track of the min and max
            cur_ele = arr[idx]
            if not stack or stack[-1] < cur_ele:
                stack.append(cur_ele)
            else:
                cur_max = stack[-1]
                while stack:
                    if stack[-1] > cur_ele:
                        stack.pop()
                    else: break
                stack.append(cur_max)
        return len(stack)