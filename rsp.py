# a continuous game of rock, paper, scissors

from enum import Enum
import random

# enum structure for choices
class Choice(Enum):
	ROCK = 0
	SCISSORS = 2
	PAPER = 5

def ask():
	choices = ["0", "2", "5", "Q"]
	user_in = ""
	while user_in.upper() not in choices:
		user_in = input("Rock (0), scissors (2) or paper (5)?\nEnter Q to quit the game\n >> ")
	return user_in

# keeps track of results
wins = 0
losses = 0


# user inputs one of the choices or to quit
user_in = ask()

while(user_in.upper() != "Q"):
	user = Choice(int(user_in))

	# randomly selects the computer's choice
	comp = Choice(random.choice([0,2,5]))

	print("You selected:", user.name)
	print("Computer selected:", comp.name)

	if(user.value - comp.value == 0):
		print("DRAW!\n")
	elif((user.value - comp.value) in [-2, -3, 5]):
			print("YOU WON!\n")
			wins += 1
	else:
		print("YOU LOST :(\n")
		losses += 1
	user_in = ask()
	
# print results
print("You won", wins, "time", end="")
if(wins > 1):
	print("s", end="")
print(" and lost", losses, "time", end="")
if(losses > 1):
	print("s", end="")
print("\nOverall,", end=" ")
if(wins - losses > 0):
	print("You WON!")
elif(wins == losses):
	print("It's a DRAW!")
else:
	print("You LOST :(")