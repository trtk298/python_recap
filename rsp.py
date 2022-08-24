# a continuous game of rock, paper, scissors

from enum import Enum
import random

class Choice(Enum):
	ROCK = 0
	SCISSORS = 2
	PAPER = 5

# keeps track of results
wins = 0
losses = 0

# randomly selects the computer's choice
comp = Choice(random.choice([0,2,5]))

# user inputs one of the choices or to quit
user_in = input("Rock (0), scissors (2) or paper (5)?\nEnter Q to quit the game\n >> ")

while(user_in.upper() != "Q"):
	user = Choice(int(user_in))
	print("You selected:", user.name)
	print("Computer selected:", comp.name)

	if(user.value - comp.value == 0):
		print("DRAW!\n")
	elif((user.value - comp.value) in [-2, -3, 5]):
			print("YOU WON!")
			wins += 1
	else:
		print("YOU LOST :(")
		losses += 1
	user_in = input("Rock (0), scissors (2) or paper (5)?\nEnter Q to quit the game\n >> ")
	
# print results
print("You won", wins, "times and lost", losses, "times")
print("Overall,", end=" ")
if(wins - losses > 0):
	print("You WON!")
elif(wins == losses):
	print("It's a DRAW!")
else:
	print("You LOST :(")