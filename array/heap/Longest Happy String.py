from heapq import heappush, heappop


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #  THE INVARIANT IS ONLY IN THE HEAP WHEN THE FREQ IS GREATER THAN 0
        h = []
        if a > 0:
            heappush(h, (-a, "a"))
        if b > 0:
            heappush(h, (-b, "b"))
        if c > 0:
            heappush(h, (-c, "c"))
        res = []
        while h:
            freq, char = heappop(h)
            # when the result is empty or when the last element in the arr is not the char we want to add at the moment
            if not res or res[-1] != char:
                to_add = min(2, -freq)
            else:
                to_add = min(1, -freq)
            for _ in range(to_add):
                res.append(char)
            if not h:
                break
            freq1, nxt_char = heappop(h)
            res.append(nxt_char)
            freq += to_add
            if freq < 0:
                heappush(h, (freq, char))
            freq1 += 1
            if freq1 < 0:
                heappush(h, (freq1, nxt_char))
        return "".join(res)
