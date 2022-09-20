#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
reminder = number
if number < 0:
	reminder = number % -10
else:
	reminder = number % 10
print("Last digit of",number,"is",reminder,end=" ")

if reminder > 5:
	print("and is greater than 5")
elif reminder == 0:
	print("and is 0")
else:
	print("and is less than 6 and not 0")
