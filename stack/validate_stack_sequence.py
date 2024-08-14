from typing import List
from collections import deque

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        '''
        pushed = [2 1 0]
        popped = [1, 2, 0]
        The main idea is simulate the operations
        '''
        pushed = deque(pushed)
        stack = []

        for x in popped:
            if len(stack) > 0 and x == stack[-1]:
                stack.pop()
                continue 

            while len(pushed) > 0 and pushed[0] != x:
                stack.append(pushed[0])
                pushed.popleft()
            
            if len(pushed) == 0:
                return False 
            
            pushed.popleft()
        return True 
        

def main():
    sol = Solution()
    pushed = [2, 1, 0]
    popped = [1, 2, 0]
    res = sol.validateStackSequences(pushed, popped)
    print(res)

if __name__ == "__main__":
    main()