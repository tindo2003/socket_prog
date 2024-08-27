from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.items = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.items[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        cur_lst = self.items[key]
        l = 0 
        r = len(cur_lst) - 1
        res = -1 
        while l <= r:
            mid = (l + r) // 2
            cur_time = cur_lst[mid][1]
            if cur_time == timestamp:
                return cur_lst[mid][0]
            elif cur_time > timestamp:
                r = mid - 1
            else:
                res = cur_lst[mid][0]
                l = mid + 1
        return res if res != -1 else ""
                


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)