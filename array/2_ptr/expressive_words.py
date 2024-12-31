from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        s += "a"

        def is_stretchy(word) -> bool:
            word += "a"
            s_ptr = idx = 0
            while idx < len(word) - 1:
                word_freq = s_freq = 1
                while idx + 1 < len(word) and word[idx] == word[idx + 1]:
                    idx += 1
                    word_freq += 1
                if s[s_ptr] != word[idx]:
                    return False
                while s_ptr + 1 < len(s) and s[s_ptr] == s[s_ptr + 1]:
                    s_freq += 1
                    s_ptr += 1
                idx += 1
                s_ptr += 1
                if s_freq == word_freq:
                    continue
                if s_freq < 3 or s_freq < word_freq:
                    return False
            if s_ptr < len(s) - 1:
                return False
            return True

        res = 0
        for word in words:
            if is_stretchy(word):
                res += 1
        return res


def main():
    sol = Solution()
    res = sol.expressiveWords("heeellooo", ["hello", "hi", "helo"])
    print(res)


if __name__ == "__main__":
    main()
