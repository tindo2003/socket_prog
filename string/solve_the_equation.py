import re


class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = [], []
        lefts, rights = equation.split("=")

        def extract_terms(expression):
            pattern = r"(-?\d*)x|(-?\d+)"  # Regex pattern with capturing groups
            matches = re.finditer(pattern, expression)

            integer = 0
            coefficient = 0
            for match in matches:
                if match.group(1) is not None:  # With anything then x
                    tmp = match.group(1)
                    if tmp == "": # "x"
                        tmp = "1"
                    elif tmp == "-": # "-x"
                        tmp = "-1"
                    coefficient += int(tmp)
                elif match.group(2):  # Standalone number
                    integer += int(match.group(2))
            return integer, coefficient

        left_int, left_coeff = extract_terms(lefts)
        right_int, right_coeff = extract_terms(rights)

        left_side = left_coeff - right_coeff
        right_side = right_int - left_int
        if left_side == 0:
            if right_side == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        res = right_side // left_side
        return f"x={res}"
