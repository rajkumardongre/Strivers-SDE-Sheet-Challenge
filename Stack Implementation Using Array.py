from os import *
from sys import *
from collections import *
from math import *

# Stack class.
class Stack:
    # arr = []
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = []
        self.top_i = -1

    def push(self, num: int) -> None:
        if(self.isFull() == 1):
            return None
        self.top_i += 1
        self.arr.append(num)
        return None

    def pop(self) -> int:
        if(self.isEmpty() == 1):
            return -1
        t = self.arr.pop()
        self.top_i -= 1
        return t
    
    def top(self) -> int:
        if(self.isEmpty() == 1):
            return -1
        return self.arr[self.top_i]

    def isEmpty(self) -> int:
        if(len(self.arr) == 0):
            return 1
        return 0
    
    def isFull(self) -> int:
        if(self.capacity == len(self.arr)):
            return 1
        return 0
