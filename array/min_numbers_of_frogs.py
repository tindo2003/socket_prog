class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        my_dict = {"c":0, "r":1, "o":2, "a":3, "k":4}
        arr = [0] * 5
        res = 0
        for c in croakOfFrogs:
            idx = my_dict[c]
            arr[idx] += 1
            if idx != 0: 
                arr[idx-1] -= 1
                if arr[idx-1] < 0: return -1
            res = max(res, sum(arr[:4]))
        if sum(arr[:4]) != 0:
            return -1 
        return res