def solution(matrix):
    n = len(matrix)

    def diff(a, b):
        return sum([abs(ele1 - ele2) for ele1, ele2 in zip(a, b)])

    options = []
    for row in matrix:
        no_shift = row
        shifted_once = row[1:] + row[:1]
        options.append((no_shift, shifted_once))

    dp = [[float("inf")] * 2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = 0

    for i in range(1, n):
        for cur in [0, 1]:
            for prev in [0, 1]:
                prev_row = options[i - 1][prev]
                cur_row = options[i][cur]
                cost = diff(cur_row, prev_row)
                dp[i][cur] = min(dp[i][cur], dp[i - 1][prev] + cost)

    print(dp)
    return min(dp[-1])


solution([[1, 4, 2, 0], [0, 2, 3, 1], [1, 0, 2, 3]])
