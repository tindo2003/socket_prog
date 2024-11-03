from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        keep_track = [0] * 26
        p_freq = [0] * 26
        l = 0 
        res = []

        def char_to_idx(c: str) -> int:
            return ord(c) - ord('a')
        def check_anagram() -> bool:
            for i in range(26):
                if keep_track[i] != p_freq[i]: return False 
            return True
        
        for c in p:
            p_freq[ord(c) - ord('a')] += 1 
        for i in range(len(p)):
            keep_track[char_to_idx(s[i])] += 1
        if check_anagram(): res.append(0)
        
        for i in range(len(p), len(s)):
            keep_track[char_to_idx(s[i])] += 1
            keep_track[char_to_idx(s[l])] -= 1
            l += 1
            if check_anagram(): res.append(l)
        return res
