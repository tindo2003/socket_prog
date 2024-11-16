class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        res = sorted(counter.items(), key=lambda x: x[1])
        idx = 0
        while k >= 0 and idx < len(res) and k >= res[idx][1]:
            k -= res[idx][1]
            idx += 1
        return len(res) - idx
        