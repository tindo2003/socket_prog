class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        possibilities = ["a", "b", "c"]
        res = []

        def recur(cur_lst):
            if len(cur_lst) >= n:
                res.append(cur_lst.copy())
                return

            for ele in possibilities:
                if not cur_lst:
                    cur_lst.append(ele)
                    recur(cur_lst)
                    cur_lst.pop()
                else:
                    if ele != cur_lst[-1]:
                        cur_lst.append(ele)
                        recur(cur_lst)
                        cur_lst.pop()

        recur([])
        res.sort()
        if k - 1 >= len(res):
            return ""
        return "".join(res[k - 1])
