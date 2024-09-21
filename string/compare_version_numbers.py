class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1 = version1.split(".")
        lst2 = version2.split(".")
        if len(lst1) < len(lst2):
            lst1 = lst1 + ["0"] * (len(lst2) - len(lst1))
        elif len(lst2) < len(lst1):
            lst2 = lst2 + ["0"] * (len(lst1) - len(lst2))

        ptr1, ptr2 = 0, 0
        while ptr1 < len(lst1):
            cur_ele1 = int(lst1[ptr1])
            cur_ele2 = int(lst2[ptr2])
            if cur_ele1 < cur_ele2:
                return -1
            elif cur_ele1 > cur_ele2:
                return 1
            ptr1 += 1
            ptr2 += 1
        return 0