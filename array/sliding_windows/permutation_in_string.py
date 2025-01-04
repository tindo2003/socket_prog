from collections import defaultdict, Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # VERY SIMILAR TO find all anagrams in string lc problem
        s1_dict = Counter(s1)
        s2_dict = defaultdict(int)

        def check_2_dict() -> bool:
            for k, v in s2_dict.items():
                if s1_dict[k] != v:
                    return False
            return True

        l = 0
        for r in range(len(s2)):
            s2_dict[s2[r]] += 1
            if r - l + 1 == len(s1):
                if check_2_dict():
                    return True
                s2_dict[s2[l]] -= 1
                l += 1

        return False
