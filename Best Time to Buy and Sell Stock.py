from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    n = len(prices)
    i = n-1
    big = 0
    small = 0
    profit = 0
    while(i >= 0):
        if(prices[i] >= big):
            big = prices[i]
            small = prices[i]
        else:
            if(big - prices[i] > profit):
                small = prices[i]
                profit = big - small
        i -= 1
    return profit