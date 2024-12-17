from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        lst = []
        res = []
        N = len(s)

        def recur(idx):
            if len(lst) == 4:
                if idx == len(s):
                    res.append(".".join(lst.copy()))
            for new_idx in range(idx + 1, min(idx + 4, N + 1)):
                if new_idx == idx + 1:
                    if s[idx:new_idx] == "0":
                        lst.append(s[idx:new_idx])
                        recur(new_idx)
                        lst.pop()
                        break
                if int(s[idx:new_idx]) > 255:
                    break
                lst.append(s[idx:new_idx])
                recur(new_idx)
                lst.pop()

        recur(0)
        return res


def main():
    sol = Solution()
    s = "101023"
    sol.restoreIpAddresses(s)


if __name__ == "__main__":
    main()
