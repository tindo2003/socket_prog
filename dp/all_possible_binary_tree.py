from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def tree_repr(self):
        res = [self.val]
        queue = [self.left, self.right]
        while queue:
            level = []
            n = len(queue)
            for _ in range(n):
                cur = queue.pop(0)
                if not cur:
                    level.append(None)
                    #res.append(None)
                else:
                    level.append(cur.val)
                   # res.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)

            # print(f"lvl {level}") 
            if level.count(None) < len(level):
                res.extend(level)

        return res
                


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        dp = {}
        def construct(x):
            if x == 0:
                return []
            if x == 1:
                return [TreeNode()]
            
            if x in dp:
                return dp[x]
            ans = []
            # 3 = (1, 1)
            # 5 = (3, 1), (1, 3) -> 2 ways
            # 7 = (5, 1), (1, 5), (3, 3)
            for left in range(1, x, 2):
                right = x - 1 - left 

                left_trees = construct(left)
                right_trees = construct(right)

                for l in left_trees:
                    for r in right_trees:
                        ans.append(TreeNode(0, l, r))
            dp[x] = ans 
            return dp[x] 

        return construct(n)

def main():
    sol = Solution()
    res = sol.allPossibleFBT(n=7)
    print([i.tree_repr() for i in res])
    print(len(res))

if __name__ == "__main__":
    main()
