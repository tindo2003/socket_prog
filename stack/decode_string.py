
class Solution:
    def decodeString(self, s: str) -> str:
        multiplier_stack = []
        prev_str_stack = []
        word = ""
        number = 0 
        idx = 0
        N = len(s)
        while idx < N:
            c = s[idx]
            if c.isdigit():
                tmp = c 
                while s[idx + 1].isdigit():
                    idx += 1
                    tmp += s[idx]
                number = int(tmp)
            elif c == "[":
                multiplier_stack.append(number)
                prev_str_stack.append(word)
                word = ""
                print(prev_str_stack)
            elif c == "]":
                multiplier = multiplier_stack.pop()
                prev_str = prev_str_stack.pop()
                word = prev_str + multiplier * word 
            elif c.isalpha():
                word += c 
            idx += 1
        return word 

def main():
    sol = Solution()
    my_str = "100[leetcode]"
    res = sol.decodeString(my_str)
    print(res)

if __name__ == "__main__":
    main()
            