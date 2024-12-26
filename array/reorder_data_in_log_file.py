from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        for idx, log in enumerate(logs):
            identifier, value = log.split(" ", 1)
            if not value[0].isdigit():
                letter.append((identifier, value, idx))
            else:
                digit.append(log)
        letter.sort(key=lambda x: (x[1], x[0]))

        res = []
        for _, _, idx in letter:
            res.append(logs[idx])
        res += digit
        return res
