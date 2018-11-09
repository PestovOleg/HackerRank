#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    x=max(ar)
    result=0
    for i in ar:
        if x==i:
            result+=1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH']+'1.txt', 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()