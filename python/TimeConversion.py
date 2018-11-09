#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
# XX:XX:XXAM
def timeConversion(s):
    if len(s)!=10 or (s[2]!=':' or s[5]!=':') or (s[8:]!='AM' and s[8:]!='PM'):
        print("Неподерживаемый формат")
        return str(False)
    result=()
    if s[8:]=='AM':
        if s[:2]=='12':
            result='00'+s[2:8]
        else:
            result=s[0:8]
    if s[8:]=='PM':
        if s[:2]!='12':
            result=str(int(s[0:2])+12)+s[2:8]
        else:
            result=s[0:8]
    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH']+'1.txt', 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()