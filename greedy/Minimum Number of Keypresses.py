from collections import Counter


class Solution:
    """
    @param s: A string
    @return: Minimum number of keypresses
    """

    def minimum_keypresses(self, s: str) -> int:
        # we make the most frequent letter to be one press
        freq = Counter(s)
        my_dict = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        counter = 1
        multiplier = 1
        res = 0
        for k, v in my_dict.items():

            if counter == 10:
                multiplier += 1
                counter = 1
            res += v * multiplier
            counter += 1
        return res
