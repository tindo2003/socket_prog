#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calculateMaxQualityScore' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER impactFactor
#  2. INTEGER_ARRAY ratings
#
from math import inf


def calculateMaxQualityScore(impactFactor, ratings):
    n = len(ratings)
    if n == 0:
        return 0

    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + ratings[i]

    def subarray_sum(L, R):
        return prefix_sum[R + 1] - prefix_sum[L]

    suffix_max = [0] * n
    suffix_max[0] = ratings[0]
    for i in range(1, n):
        suffix_max[i] = max(ratings[i], suffix_max[i - 1] + ratings[i])

    best_suffix_up_to = [0] * n
    best_suffix_up_to[0] = suffix_max[0]
    for i in range(1, n):
        best_suffix_up_to[i] = max(best_suffix_up_to[i - 1], suffix_max[i])

    prefix_max = [0] * n
    prefix_max[n - 1] = ratings[n - 1]
    for i in range(n - 2, -1, -1):
        prefix_max[i] = max(ratings[i], prefix_max[i + 1], ratings[i])

    best_prefix_from = [0] * n
    best_prefix_from[n - 1] = prefix_max[n - 1]
    for i in range(n - 2, -1, -1):
        best_prefix_from[i] = max(best_prefix_from[i + 1], prefix_max[i])

    best_amplify = -inf
    for L in range(n):
        for R in range(L, n):
            original_sub_sum = subarray_sum(L, R)
            amplified_sum = original_sub_sum * impactFactor

            left_part = 0
            if L > 0:
                left_part = best_suffix_up_to[L - 1]

            right_part = 0
            if R < n - 1:
                right_part = best_prefix_from[R + 1]

            candidate1 = amplified_sum
            candidate2 = left_part + amplified_sum
            candidate3 = amplified_sum + right_part
            candidate4 = left_part + amplified_sum + right_part

            best_local = max(candidate1, candidate2, candidate3, candidate4)
            best_amplify = max(best_amplify, best_local)

    def adjusted(x, factor):
        if x >= 0:
            return x // factor
        else:
            return -((-x) // factor)

    delta = [0] * n
    for i in range(n):
        new_val = adjusted(ratings[i], impactFactor)
        delta[i] = new_val - ratings[i]

    best_adjust = -inf
    for L in range(n):
        for R in range(L, n):
            original_sub_sum = subarray_sum(L, R)
            delta_sum = sum(delta[L : R + 1])
            adjusted_sub_sum = original_sub_sum + delta_sum

            left_part = 0
            if L > 0:
                left_part = best_suffix_up_to[L - 1]

            right_part = 0
            if R < n - 1:
                right_part = best_prefix_from[R + 1]

            candidate1 = adjusted_sub_sum
            candidate2 = left_part + adjusted_sub_sum
            candidate3 = adjusted_sub_sum + right_part
            candidate4 = left_part + adjusted_sub_sum + right_part
            best_local = max(candidate1, candidate2, candidate3, candidate4)
            best_adjust = max(best_adjust, best_local)

    return max(best_amplify, best_adjust)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    impactFactor = int(input().strip())

    ratings_count = int(input().strip())

    ratings = []

    for _ in range(ratings_count):
        ratings_item = int(input().strip())
        ratings.append(ratings_item)

    result = calculateMaxQualityScore(impactFactor, ratings)

    fptr.write(str(result) + "\n")

    fptr.close()
