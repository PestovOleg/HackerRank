#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    result=1
    for i in range(n+1):
        #print(result)
        if i%2==1:
            result+=1
        else:
            result*=2
    return result
#        result=1 if (i>1) else result=2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH']+'1.txt', 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()