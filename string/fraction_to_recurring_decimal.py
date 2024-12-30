from collections import defaultdict


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = []
        m = defaultdict(int)
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            res.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        div, remainder = divmod(numerator, denominator)
        res.append(str(div))
        if remainder == 0:
            return "".join(res)
        res.append(".")
        while remainder != 0:
            if remainder in m:
                idx = m[remainder]
                res = res[0:idx] + ["("] + res[idx:] + [")"]
                break
            m[remainder] = len(res)
            div, remainder = divmod(remainder * 10, denominator)
            res.append(str(div))
        return "".join(res)
