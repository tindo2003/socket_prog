from typing import List


class Solution:
    def findReplaceString(
        self, s: str, indices: List[int], sources: List[str], targets: List[str]
    ) -> str:
        # keep track which index of sources/targets to use to replace a range of indices in s
        res = []
        index_to_replace = [-1] * len(s) # index in s -> index in sources/targets (if any)
        for idx, val in enumerate(indices):
            length_of_substr = len(sources[idx])
            if s[val : val + length_of_substr] == sources[idx]:
                index_to_replace[val] = idx
        s_idx = 0
        while s_idx < len(s):
            if index_to_replace[s_idx] == -1:
                res.append(s[s_idx])
                s_idx += 1
            else:
                target_idx = index_to_replace[s_idx]
                res.append(targets[target_idx])
                s_idx += len(sources[target_idx])
        return "".join(res)
