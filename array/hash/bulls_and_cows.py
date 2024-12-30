from collections import defaultdict, Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = defaultdict(int)
        cows = defaultdict(int)
        cows_cnt = bulls_cnt = 0
        secret_freq = Counter(secret)
        guess_freq = Counter(guess)
        for idx, val in enumerate(guess):
            if val == secret[idx]:
                bulls[val] += 1
                bulls_cnt += 1
        for k, v in guess_freq.items():
            cows[k] = min(v, secret_freq[k]) - bulls[k]
            if cows[k] > 0:
                cows_cnt += cows[k]

        return f"{bulls_cnt}A{cows_cnt}B"
