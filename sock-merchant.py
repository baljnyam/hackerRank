import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
count = 0
def sockMerchant(n, ar):
    for i in range(0, len(ar)):
        for j in range(i+1, len(ar)):
            if ar[i] == ar[j]:
                ar.remove(ar[i])
                ar.remove(ar[j])
                ++count
    return count

if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
