class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)
        num_y_right = [0] * (N + 1)
        num_n_left = [0] * (N + 1)
        num1 = 0
        for idx in range(N + 1):
            if idx < len(customers):
                val = customers[idx]
                if val == "N":
                    num1 += 1
            num_n_left[idx] = num1
        num1 = 0
        for idx in range(len(customers), -1, -1):
            if idx < len(customers):
                val = customers[idx]
                if val == "Y":
                    num1 += 1
            num_y_right[idx] = num1

        min_idx = -1
        min_val = inf
        for i in range(len(customers) + 1):
            left = 0
            if i >= 1:
                left = num_n_left[i - 1]
            right = num_y_right[i]
            total = right + left
            if total < min_val:
                min_val = right + left
                min_idx = i
        return min_idx
