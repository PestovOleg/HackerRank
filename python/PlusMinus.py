#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    a=b=c=0
    for i in arr:
        if i>0:
            a+=1
        elif i<0:
            b+=1
        else:
            c+=1
    print(round(a/len(arr),6))
    print(round(b/len(arr),6))
    print(round(c/len(arr),6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)