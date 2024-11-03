from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        #WATCH https://www.youtube.com/watch?v=lx7sXPATO3U&ab_channel=AryanMittal
        ptr = 0 
        iter_idx = list(range(len(deck)))
        deck.sort()
        q = deque(iter_idx)
        res = [0] * len(deck)
        # simulating the queue 
        even = True
        while q:
            top = q.popleft()
            if even:
                res[top] = deck[ptr]
                ptr += 1
                even = False
            else:
                q.append(top)
                even = True
        return res
            
