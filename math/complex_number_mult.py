class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # (a + bi) * (c + di)
        # ac +  (ad+bc)i +   -bd
        lst1 = num1.split("+")
        real1, imagine1 = int(lst1[0]), int(lst1[1][:-1])
        lst2 = num2.split("+")
        real2, imagine2 = int(lst2[0]), int(lst2[1][:-1])
        ac = real1 * real2
        adbc = real1 * imagine2 + imagine1 * real2
        bd = imagine1 * imagine2
        res_real = ac - bd
        return f"{res_real}+{adbc}i"