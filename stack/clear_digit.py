class Solution:
    def clearDigits(self, s: str) -> str:
        digit_stack = []
        nondigit_stack = []
        for idx, c in enumerate(s):
            if c.isdigit():
                if nondigit_stack:
                    nondigit_stack.pop()
                else:
                    digit_stack.append((idx, c))
            else:
                nondigit_stack.append((idx, c))
        new_str = [""] * len(s)
        for idx, val in nondigit_stack:
            new_str[idx] = val
        for idx, val in digit_stack:
            new_str[idx] = val
        return "".join(new_str)
