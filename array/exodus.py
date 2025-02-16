def check_permutations(p):
    """
    p is a list of integers from 0 to n-1, where n is the length of p.
    """
    n = len(p)
    # keep track of indices of all elements in p
    indices = [0] * (n + 1)
    for i in range(n):
        indices[p[i]] = i + 1

    res = ["0"] * n
    min_idex = indices[1]
    max_index = indices[1]
    res[0] = "1"
    for k in range(2, n + 1):
        min_idex = min(min_idex, indices[k])
        max_index = max(max_index, indices[k])
        length_of_block = max_index - min_idex + 1
        if length_of_block == k:
            res[k - 1] = "1"
        else:
            res[k - 1] = "0"
    return "".join(res)
