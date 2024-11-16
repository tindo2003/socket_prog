class TimeMap:

    def __init__(self):
        self.keyToTime = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyToTime:
            self.keyToTime[key] = [(timestamp, value)]
        else:
            self.keyToTime[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyToTime:
            return ""
        my_arr = self.keyToTime[key]
        idx = self.bin_search(timestamp, my_arr)
        if idx == -1:
            return ""
        return my_arr[idx][1]

    def bin_search(self, tgt, arr):
        # find element <= tgt
        l, r = 0, len(arr) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            mid_ele = arr[mid][0]
            if mid_ele <= tgt:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
