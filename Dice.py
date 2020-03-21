
import random

class Dice:

	sides = " " #variable to hold the sides of the dice.

	def __init__(self,sides):
		self.sides = sides

	def roll(self):
		return random.randint(1, self.sides)





sides = int(input("Enter the sided die you would like to roll: "))
numberOfDice = int(input("Enter how may dice you would like to roll: "))

for x in range(1,numberOfDice+1):
	print('D{} {}: {}'.format(sides,x,Dice(sides).roll()))