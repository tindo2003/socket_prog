class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def bit_to_arr(num):
            count = 0
            arr = [0] * 30
            idx = 29
            while num != 0:
                arr[idx] = num % 2
                if num % 2 == 1:
                    count += 1
                num = num // 2
                idx -= 1
            return count, arr

        def count_1(num):
            counter = 0
            while num != 0:
                if num % 2 == 1:
                    counter += 1
                num = num // 2
            return counter

        actual, arr = bit_to_arr(num1)
        to_take = count_1(num2)

        if actual == to_take:
            # print("this case")
            return num1
        elif actual > to_take:
            # want to keep the remaining MSB so that XOR will get rid of the MSBs
            idx = 29
            while idx > 0:
                if actual == to_take:
                    break
                if arr[idx] == 1:
                    arr[idx] = 0
                    actual -= 1
                idx -= 1
            map_str = map(str, arr)
            tmp_str = "".join(map_str)
            return int(tmp_str, 2)
        elif actual < to_take:
            # there is more to add to match the number of set bits
            more_to_add = to_take - actual
            idx = 29
            while more_to_add > 0 and idx > 0:
                if arr[idx] == 0:
                    arr[idx] = 1
                    more_to_add -= 1
                idx -= 1
            map_str = map(str, arr)
            tmp_str = "".join(map_str)
            return int(tmp_str, 2)
