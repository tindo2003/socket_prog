from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []

        def dfs(idx, bit_lst, res_lst):
            # difference in bits between 2 adjacent elements is 1
            if idx >= n:
                print(bit_lst)
                res.append(res_lst.copy())
                return
            for i in [0, 1]:
                bit_lst.append(i)
                if idx == 0:
                    res_lst.append(i)
                else:
                    res_lst.append(bit_lst[idx] ^ bit_lst[idx - 1])
                dfs(idx + 1, bit_lst, res_lst)

                bit_lst.pop()
                res_lst.pop()

        bit_lst = []
        res_lst = []
        dfs(0, bit_lst, res_lst)
        print(res)
        for idx, item in enumerate(res):
            res[idx] = int("".join(list(map(str, item))), 2)
        return res


def main():
    sol = Solution()
    res = sol.grayCode(3)
    print(res)


if __name__ == "__main__":
    main()
