class SnapshotArray:

    def __init__(self, length: int):
        self.array = [
            [] for _ in range(length)
        ]  # Each index's history: list of (snap_id, value)
        self.current_snap_id = 0

    def set(self, index: int, val: int) -> None:
        history = self.array[index]
        if history and self.current_snap_id == history[-1][0]:
            history[-1] = (self.current_snap_id, val)
        else:
            history.append((self.current_snap_id, val))

    def snap(self) -> int:
        snap_id = self.current_snap_id
        self.current_snap_id += 1
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        history = self.array[index]
        # print(history)
        left, right = 0, len(history) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if history[mid][0] <= snap_id:
                left = mid + 1
                res = mid
            else:
                right = mid - 1
        if res == -1:
            return 0
        return history[res][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
