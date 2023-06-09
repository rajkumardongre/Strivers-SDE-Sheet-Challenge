from os import *
from sys import *
from collections import *
from math import *

denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
	coin = 0
	while(amount > 0):
		if(amount >= 1000):
			coin += amount//1000
			amount = amount%1000
		elif(amount >= 500):
			coin += amount//500
			amount = amount%500
		elif(amount >= 100):
			coin += amount//100
			amount = amount%100
		elif(amount >= 50):
			coin += amount//50
			amount = amount%50
		elif(amount >= 20):
			coin += amount//20
			amount = amount%20
		elif(amount >= 10):
			coin += amount//10
			amount = amount%10
		elif(amount >= 5):
			coin += amount//5
			amount = amount%5
		elif(amount >= 2):
			coin += amount//2
			amount = amount%2
		else:
			coin += 1
			amount -= 1
	return coin
		