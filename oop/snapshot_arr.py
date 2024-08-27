class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((val, self.snap_id))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        N = len(self.arr[index])
        for i in range(N-1, -1, -1):
            val, my_id = self.arr[index][i]
            #always get the most up-to-date
            if my_id <= snap_id:
                return val