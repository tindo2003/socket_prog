from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)
        level_num = 0
        q = [root]
        while q:
            for idx in range(len(q)):
                cur = q.pop(0)
                if cur.left:
                    levels[level_num].append(cur.left.val)
                    q.append(cur.left)
                if cur.right:
                    levels[level_num].append(cur.right.val)
                    q.append(cur.right)
            level_num += 1
        res = 0

        for k, level in levels.items():
            cnt = self.count_swap(level)
            res += cnt
        return res

    def count_swap(self, arr):
        N = len(arr)
        original = [(val, idx) for idx, val in enumerate(arr)]
        sorted_arr = sorted(original)
        visited = [False] * N
        swaps = 0

        for i in range(N):
            if visited[i] or original[i][1] == sorted_arr[i][1]:
                continue

            cycle_length = 0
            x = i
            while not visited[x]:
                visited[x] = True
                x = sorted_arr[x][1]
                cycle_length += 1

            if cycle_length > 1:
                swaps += cycle_length - 1

        return swaps

    # selection sort inspired
    # def count_swap(self, arr):
    #     N = len(arr)
    #     cnt = 0
    #     for idx in range(N):
    #         min_idx = idx
    #         for j in range(idx + 1, N):
    #             if arr[j] < arr[min_idx]:
    #                 min_idx = j
    #         if min_idx == idx: continue
    #         cnt += 1
    #         arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
    #     return cnt
