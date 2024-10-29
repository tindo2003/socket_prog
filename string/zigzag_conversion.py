class Solution:
    def convert(self, s: str, numRows: int) -> str:
        max_idx = 2 * numRows - 2
        res = []
        if numRows == 1:
            return s
        start = 1
        for start_idx in range(numRows):
            if start_idx == 0 or start_idx == numRows - 1:
                for next_idx in range(start_idx, len(s), numRows - 1 + numRows - 1):
                    res.append(s[next_idx])
            else:
                bigger = max_idx - start * 2
                smaller = max_idx - bigger
                tmp = start_idx
                while tmp < len(s):
                    if tmp < len(s):
                        res.append(s[tmp])
                    tmp += bigger
                    if tmp < len(s):
                        res.append(s[tmp])
                    tmp += smaller
                start += 1
        return "".join(res)
