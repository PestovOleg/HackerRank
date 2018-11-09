import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    a=b=x=y=0
    i=len(arr)
    for _ in range(i):
        a+=arr[x][x]
        x+=1
    x=0
    y=i-1
    for _ in range(i):
        b+=arr[x][y]
        x+=1
        y-=1
    return int(math.fabs(a-b))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH']+'1.txt', 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()