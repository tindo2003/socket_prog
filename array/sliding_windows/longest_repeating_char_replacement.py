from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counter = defaultdict(int)
        max_count = float("-inf")
        res = float("-inf")
        for r, c in enumerate(s):
            counter[c] += 1
            if counter[c] > max_count:
                max_count = counter[c]
            # window length - max count = the number of characters that need to be replaced. if the # of replacement > k, shrink the window
            while ((r - l + 1 - max_count) > k):
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res 


def main():
    sol = Solution()
    s = "AABABBA"
    k = 1
    res = sol.characterReplacement(s, k)
    print(res)

if __name__ == "__main__":
    main()


