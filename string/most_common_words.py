import re
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = re.findall(r"\b\w+\b", paragraph)
        words = [item.lower() for item in words]
        words = list(filter(lambda x: x not in banned, words))
        freq = Counter(words)
        freq = [(k, v) for k, v in freq.items()]
        freq.sort(key=lambda x: x[1], reverse=True)
        return freq[0][0]
