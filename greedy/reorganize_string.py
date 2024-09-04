from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        s_lst = list(s)
        N = len(s_lst)
        counter = Counter(s_lst)
        h = []
        for char, freq in counter.items():
            heapq.heappush(h, (-freq, char))
        
        even = False
        idx = 0 
        res = [""] * N
        while h:
            freq, c = heapq.heappop(h)
            freq *= -1
            #print("c", c, "freq", freq)
            while freq > 0:
                res[idx] = c
                if (idx > 0 and res[idx-1] == c) or (idx < N-1 and res[idx+1] == c):
                    return ""
                if idx + 2 >= N:
                    if even:
                        idx = 0 
                    else:
                        idx = 1
                    even = not even
                else:
                    idx += 2
                freq -= 1
            #print(res)
        return "".join(res)


def main():
    sol = Solution()
    s = "aaab"
    res = sol.reorganizeString(s)
    print(res)

if __name__ == "__main__":
    main()