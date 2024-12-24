class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s = ""
        n = 0
        if len(str1) < len(str2):
            s = str1
            n = len(str1)
        else:
            s = str2
            n = len(str2)
        res = ""

        def prefix_match_string(prefix, s):
            offset = len(prefix)
            for i in range(0, len(s), offset):
                if i + offset > len(s):
                    return False
                if s[i : i + offset] != prefix:
                    return False
            return True

        def check_prefix(prefix, s1, s2) -> bool:
            offset = len(prefix)
            if len(prefix) > len(s1) or len(prefix) > len(s2):
                return False
            if not prefix_match_string(prefix, s1):
                return False
            if not prefix_match_string(prefix, s2):
                return False
            return True

        for idx in range(n):
            prefix = s[: idx + 1]
            if check_prefix(prefix, str1, str2):
                res = prefix
        return res
