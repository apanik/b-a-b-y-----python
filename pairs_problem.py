#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    for i in ar[:]:
        total_i = ar.count(i)
        if total_i % 2 == 0:
            pairs += total_i / 2
        else:
            total_i = total_i-1
            pairs += total_i / 2
        for j in ar[:]:
            if j == i:
                ar.remove(j)
    return int(pairs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
