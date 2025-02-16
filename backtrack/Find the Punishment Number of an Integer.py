class Solution:
    def punishmentNumber(self, n: int) -> int:
        # 1 2 3
        # 12+3, 1+23, 123+0, 1+2+3
        # picked or no picked is essential here. https://www.youtube.com/watch?v=CX2X5knWTVs&ab_channel=AlgorithmsCasts
        def recur(l, cur_idx, cur_str, cur_lst, accumulator):
            if cur_idx == len(cur_str):
                accumulator.append(cur_lst.copy())
                return
            # keep growing the partition. however, when you are at the last element, you have no choice but to add the amount u accumulatted to the end
            if cur_idx != len(cur_str) - 1:
                recur(l, cur_idx + 1, cur_str, cur_lst, accumulator)
            # break off and start a new partition
            cur_lst.append(int(cur_str[l : cur_idx + 1]))
            recur(cur_idx + 1, cur_idx + 1, cur_str, cur_lst, accumulator)
            cur_lst.pop()

        res = 0
        for new_num in range(n + 1):
            squared = new_num * new_num
            new_num_str = str(squared)
            accumulator = []
            recur(0, 0, new_num_str, [], accumulator)
            for item in accumulator:
                su = sum(item)
                if su == new_num:
                    res += squared
                    break
        return res
