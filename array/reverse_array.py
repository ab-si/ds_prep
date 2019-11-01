#!/bin/python3

import math
import os
import random
import re
import sys

def reverse_slice(ar):
    return ar[::-1]

def reversed_bltin(ar):
    return [ele for ele in reversed(ar)]

def reverse_bltin(ar):
    ar.reverse()
    return ar

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    res = reverse_bltin(arr)
    print(res)
