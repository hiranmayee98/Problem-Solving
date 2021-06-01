import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    st=" "
    for j in range(1,n):
        i=j-1
        key=arr[j]
        while i>=0 and arr[i]>key:
            arr[i+1]=arr[i]
            i=i-1
            st=" ".join(str(ele) for ele in arr)
            print(st)
        arr[i+1]=key
    st=" ".join(str(ele) for ele in arr)
    print(st)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
