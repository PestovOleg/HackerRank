#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_max=0
    sum_min=sum(arr)
    
    for i in range(len(arr)):
        tmp=arr.copy()
        tmp.pop(i)
        if sum(tmp)>sum_max:
            sum_max=sum(tmp)
        if sum(tmp)<sum_min:
            sum_min=sum(tmp)
    print(str(sum_min)+" " +str(sum_max))



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)