#!/bin/python3
'''input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
'''
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
t = [sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3]) for i in range(len(arr)-2) for j in range(len(arr[i])-2)]
print(max(t))






