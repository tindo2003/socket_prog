class Solution:
    def partitionString(self, s: str) -> int:
        n = len(s)
        res = 0
        my_set = set()
        for i in range(n):
            cur_ele = s[i]
            if cur_ele in my_set:
                res += 1
                my_set = set([cur_ele])
            else:
                my_set.add(cur_ele)
        return res + 1
