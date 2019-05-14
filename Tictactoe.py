def display_board(board):
	"""
	Function to display the grid
	"""
	print(board[1]+'|'+board[2]+'|'+board[3])
	print('-|-|-')
	print(board[4]+'|'+board[5]+'|'+board[6])
	print('-|-|-')
	print(board[7]+'|'+board[8]+'|'+board[9])

def check_result(board):
	"""
	Function to check if someone has won the game
	"""
	if board[1]==board[2]==board[3]:
		return True
	elif board[4]==board[5]==board[6]:
		return True
	elif board[7]==board[8]==board[9]:
		return True
	elif board[1]==board[4]==board[7]:
		return True
	elif board[2]==board[5]==board[8]:
		return True
	elif board[3]==board[6]==board[9]:
		return True
	elif board[1]==board[5]==board[9]:
		return True
	elif board[3]==board[5]==board[7]:
		return True
	return False

def isvalid_move(board,index):
	"""
	Function to check invalid player inputs
	"""
	if index<1 or index>9:
		return False
	return not( 'X' in board[index] or 'O' in board[index] )

def record_move(board,player,index):
	"""
	Function to record player move
	"""
	board[index]=player
	return board

def isboard_full(board):
	"""
	Function to check if there are any moves left
	"""
	for i in range(1,10):
		if board[i]!='X' and board[i]!='O':
			return False
	return True

#Main Driver Program
#Grid visualised as 3x3
board = ['#','1','2','3','4','5','6','7','8','9']
players = [' ']*3
player1=input("Player1 select X or O")
if player1=='X':
	players[1]='X'
	players[2]='O'
else:
	players[1]='O'
	players[2]='X'

display_board(board)
result=False
chance=1
while not result:
	
	if chance==1:
		index=int(input("player1 enter any number from 1-9"))
		if isvalid_move(board,index):
			record_move(board,players[chance],index)
		else:
			print("Invaild move")
			continue
		
		result = check_result(board)
		if not result:
			if isboard_full(board):
				break		

		display_board(board)
		chance=2
	else:
		index=int(input("player2 enter any number from 1-9"))
		if isvalid_move(board,index):
			record_move(board,players[chance],index)
		else:
			print("Invaild move")
			continue

		result = check_result(board)
		if not result:
			if isboard_full(board):
				break	
				
		display_board(board)
		chance=1

if chance==1:chance=2
else: chance=1

if not result:
	print("Game drawn!")
else:
	print("player{} wins!".format(chance))
display_board(board)
