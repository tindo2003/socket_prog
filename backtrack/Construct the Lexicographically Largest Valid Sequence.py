from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        occupied = [False] * (2 * n - 1)
        res = [0] * (2 * n - 1)
        contained = set()

        def recur(cur_idx, res, occupied):
            if cur_idx >= 2 * n - 1:
                return True
            good = False
            if not occupied[cur_idx]:
                for cur_num in range(n, 0, -1):
                    if cur_num in contained:
                        continue
                    next_idx = cur_idx + cur_num
                    if cur_num == 1:
                        res[cur_idx] = 1
                        contained.add(1)
                        if not recur(cur_idx + 1, res, occupied):
                            contained.remove(1)
                            occupied[cur_idx] = False
                        else:
                            good = True
                            break
                    else:
                        if next_idx < (2 * n - 1) and not occupied[next_idx]:
                            occupied[next_idx] = True
                            res[cur_idx] = cur_num
                            res[next_idx] = cur_num
                            contained.add(cur_num)
                            if not recur(cur_idx + 1, res, occupied):
                                occupied[next_idx] = False
                                occupied[cur_idx] = False
                                contained.remove(cur_num)
                            else:
                                good = True
                                # we want the lexicographically largest sequence
                                break
                return good
            else:
                return recur(cur_idx + 1, res, occupied)

        recur(0, res, occupied)
        return res

def main():
    sol = Solution()
    print(sol.constructDistancedSequence(3))


if __name__ == "__main__":
    main()
