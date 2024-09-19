class Solution:
    def calculate(self, s: str) -> int:
        num_stack = [] # keep track of previous seen numbers
        prev_op = "+"
        cur_num = 0
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif not c.isspace():
                if prev_op == "+":
                    num_stack.append(cur_num)
                elif prev_op == "-":
                    num_stack.append(-1 * cur_num)
                elif prev_op == "*":
                    top = num_stack.pop()
                    res = top * cur_num
                    num_stack.append(res)
                elif prev_op == "/":
                    top = num_stack.pop()
                    res = int(top / cur_num) # round toward 0
                    num_stack.append(res)
                cur_num = 0
                prev_op = c
        # for cases like, [3 - 4]. When i encounter the - sign, I add 3 into the stack since my initial prev_op is +. prev_op now becomes -. After iterating thorugh the array, I would need to do something with cur_number which is 4 in the example. since prev_op is negative, I add -4 into the stack.
        if prev_op == "+":
            num_stack.append(cur_num)
        elif prev_op == "-":
            num_stack.append(-1 * cur_num)
        elif prev_op == "*":
            top = num_stack.pop()
            res = top * cur_num
            num_stack.append(res)
        if prev_op == "/":
            top = num_stack.pop()
            res = int(top / cur_num)
            num_stack.append(res)
                    
        return sum(num_stack)
