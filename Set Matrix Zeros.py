from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    r = len(matrix)
    c = len(matrix[0])
    # print(r, c)
    row = {}
    col = {}
    for i in range(r):
        row[i] = False
    for i in range(c):
        col[i] = False
    
    for i in range(r):
        for j in range(c):
            if(matrix[i][j] == 0):
                row[i] = True
                col[j] = True
    
    for i in range(r):
        for j in range(c):
            if(row[i] or col[j]):
                matrix[i][j] = 0
    

