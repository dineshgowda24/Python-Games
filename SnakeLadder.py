import random
import os
import time

#Snakes and Ladders
ladders = { 11:24,34:45,55:74,83:96 }
snakes = { 14:5,32:13,49:26,65:39,99:69 }
player1 = 0
player2 = 0

def roll_dice():
	"""
	Function to roll the dice
	"""
	return random.randrange(1,7)

def welcome():
	"""
	Function print welcome message
	"""
	print("------------------------------")
	print("|Welcome to Snake and Ladders|")
	print("------------------------------")
	print("The snakes are at location : {}".format(list(snakes.keys())))
	print("The ladders are at location : {}".format(list(ladders.keys())))
	print("\n")
	
def is_bitten(value):
	"""
	Function to check if snake is at a given location
	"""
	if value in list(snakes.keys()):
		return True
	return False

def can_climb(value):
	"""
	Function to check if ladder is at a given location
	"""
	if value in list(ladders.keys()):
		return True
	return False

def screen_clear():
   if os.name == 'nt':
      _ = os.system('cls')
   # for mac and linux(here, os.name is 'posix')
   else:
      _ = os.system('clear')

"""
Main Driver 
"""
if __name__ == "__main__":
	
	welcome()
	turn = random.randrange(1,3)
	print("Player {} will go first".format(turn))
	
	while player1 != 100 and player2 != 100:
		print("Player1 is at {} and Player2 is at {}".format(player1,player2))
		input("Player {} Press enter to roll dice".format(turn))
		print("Rolling dice..")
		
		if turn == 1:
			value = roll_dice()
			print("Player 1 Dice {}".format(value))
			if is_bitten(player1+value) :
				print("OOPS !! Bitten by snake at {}".format(player1+value))
				player1=snakes[player1+value]
			elif can_climb(player1+value):
				print("WOW !! Ladder found at {}".format(player1+value))
				player1=ladders[player1+value]
			elif player1+value > 100:
				print("Can move forward")
			else:
				player1=player1+value
			
			if value == 6:
				print("Full Dice!! Player 1 can go again")
				turn=1
			else:
				turn=2
		else:
			value = roll_dice()
			print("Dice {}".format(value))
			if is_bitten(player2+value):
				print("OOPS !! Bitten by snake at {}".format(player2+value))
				player2=snakes[player2+value]
			elif can_climb(player2+value):
				print("WOW !! Ladder found at {}".format(player2+value))
				player2=ladders[player2+value]
			elif player2+value > 100:
				print("Can move forward")
			else:
				player2=player2+value
			
			if value == 6:
				print("Full Dice!! Player 2 can go again")
				turn=2
			else:
				turn=1
				
		time.sleep(1)
		screen_clear()
		welcome()
		
	if player1==100:
		print("Player1 wins!!")
	elif player2==100:
		print("Player2 wins!!")
