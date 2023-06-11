from os import *
from sys import *
from collections import *
from math import *

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue :

    # Define data members and __init__()
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    '''----------------- Public Functions of Queue -----------------'''

   
    def isEmpty(self) :
        return self.size == 0



    def enqueue(self, data) :
        n = Node(data)
        if(self.isEmpty()):
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.size += 1


    def dequeue(self) :
        if(self.isEmpty()):
            return -1
        top = self.head.data
        self.head = self.head.next
        self.size -= 1
        return top


    def front(self) :
        if(self.isEmpty()):
            return -1
        top = self.head.data
        return top
