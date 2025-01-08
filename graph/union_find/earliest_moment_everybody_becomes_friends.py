from typing import List


class Solution:
    """
    @param logs: Logging with time, x, y
    @param n: Total count of people
    @return: Timestamp of when everyone became friends
    """

    def earliest_acq(self, logs: List[List[int]], n: int) -> int:
        # write your code here
        parents = [i for i in range(100)]

        def find_parent(x):
            while parents[x] != x:
                x = parents[x]
            return x

        def is_connected():
            my_set = set()
            for i in range(n):
                parent = find_parent(i)
                my_set.add(parent)
                if len(my_set) > 1:
                    return False
            return True

        sorted_logs = sorted(logs, key=lambda x: x[0])  # sort by time
        for t, x, y in sorted_logs:
            x_parent = find_parent(x)
            y_parent = find_parent(y)
            parents[x_parent] = y_parent
            if is_connected():
                return t
        return -1
