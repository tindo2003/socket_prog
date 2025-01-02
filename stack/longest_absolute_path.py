import re


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        my_lst = []
        pattern = r"(^\t*)"
        for line in input.splitlines():
            match = re.match(pattern, line)
            name = line.strip("\t")
            tab_num = len(match.group(1))
            if match:
                my_lst.append((name, tab_num))
        maxi = 0
        cur_length = 0
        stack = []

        for cur_direc, cur_level in my_lst:
            while stack and (cur_level - stack[-1][1]) != 1:
                direc_name, direc_level = stack.pop()
                cur_length -= len(direc_name)
            stack.append((cur_direc, cur_level))

            cur_length += len(cur_direc)
            if "." in stack[-1][0]:
                maxi = max(maxi, cur_length + len(stack) - 1)
        return maxi
