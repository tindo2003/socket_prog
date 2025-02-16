class Solution:
    def smallestNumber(self, pattern: str) -> str:
        my_lst = []
        wanted_length = len(pattern) + 1

        def generate_all_strings(cur_lst, cur_idx):
            if len(cur_lst) == wanted_length:
                my_lst.append("".join(cur_lst))
                return
            if cur_lst:
                direction = pattern[cur_idx]
                nxt_idx = cur_idx + 1
                lst_ele = int(cur_lst[-1])
                if direction == "I":
                    for i in range(lst_ele + 1, 10):
                        if str(i) not in cur_lst:
                            cur_lst.append(str(i))
                            generate_all_strings(cur_lst, nxt_idx)
                            cur_lst.pop()
                else:
                    for i in range(1, lst_ele):
                        if str(i) not in cur_lst:
                            cur_lst.append(str(i))
                            generate_all_strings(cur_lst, nxt_idx)
                            cur_lst.pop()
            else:
                for i in range(1, 10):
                    if str(i) not in cur_lst:
                        cur_lst.append(str(i))
                        generate_all_strings(cur_lst, 0)
                        cur_lst.pop()

        generate_all_strings([], 0)
        my_lst.sort()
        # print(my_lst)
        return my_lst[0]


# insane recursive solution
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []

        def recur(cur_idx, cur_cnt) -> int:
            if cur_idx == len(pattern):
                res.append(str(cur_cnt + 1))
                return cur_cnt + 1
            else:
                if pattern[cur_idx] == "I":
                    recur(cur_idx + 1, cur_idx + 1)
                else:
                    cur_cnt = recur(cur_idx + 1, cur_cnt)
                res.append(str(cur_cnt + 1))
                return cur_cnt + 1

        recur(0, 0)
        return "".join(res[::-1])
