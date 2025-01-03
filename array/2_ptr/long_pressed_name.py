class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name += "1"
        typed += "1"
        ptr1 = ptr2 = 0
        n1 = len(name)
        n2 = len(typed)
        while ptr1 < n1 - 1:
            str1_freq = str2_freq = 0
            if ptr2 > n2 or name[ptr1] != typed[ptr2]:
                return False
            while name[ptr1] == name[ptr1 + 1]:
                str1_freq += 1
                ptr1 += 1
            while typed[ptr2] == typed[ptr2 + 1]:
                str2_freq += 1
                ptr2 += 1
            if str1_freq > str2_freq:
                return False
            ptr1 += 1
            ptr2 += 1
        if ptr2 < len(typed) - 1:
            return False
        return True
