from random import randint
# Initialize Game Board
print("Tic Tac Toe \n")
def print_grid(grid):
    for row in grid:
        print(row)

# Function to determine if a winning configuration has ocurred
def check_winner(user,comp):
	wins = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,5,7],[3,6,9],[4,5,6],[7,8,9]]
	for win in wins:
		if all(item in user for item in win):
			return "user wins",True
		elif all(item in comp for item in win):
			return "computer wins",True
	return "no winner",False

def find_best_move(user,comp):
	moves = []
	wins = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,5,7],[3,6,9],[4,5,6],[7,8,9]]
	for win in wins:
		#moves = [value for value in comp if value in win]
		if any(item in comp for item in win):
			moves.append(win)
	return moves

			

# Game board
b = [[0,0,0],
	[0,0,0],
	[0,0,0]]
print_grid(b)
print()
# Request and validate user input
while True:
    try:
        user = input('Choose x or o ')
        assert len(user) < 2 and type(user) == str
    except AssertionError:
        print("Invalid! Please enter x or o")
    else:
        break
# Set computer symbol
if user == "x" or "X":
	comp = "o"
else:
	comp = "x" 
# Initialize dictionaries and lists that track possible moves and already made moves
valid_squares = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}
taken_squares = []
user_squares = []
comp_squares = []
winner = False
while len(taken_squares) <= 8 or winner == False:
	user_choice = input("Pick Row and Column (r,c) ")
	user_choice = user_choice.split(",")
	user_choice = [int(user_choice[0])-1,int(user_choice[1])-1]
	
	for key in valid_squares.keys():
		if valid_squares.get(key) == user_choice:
			if key in taken_squares:
				print("That square is already taken")
				continue
			else:
				taken_squares.append(key)
				user_squares.append(key)
				print()
				b[user_choice[0]][user_choice[1]] = user

				if len(taken_squares) > 8:
					break
				valid = 0
				while not valid: # Gets a valid computer move based on free spaces
					moves = find_best_move(user_squares,comp_squares)
					#if len(moves) == 0:
						#comp_choice = randint(1,9)
					print(moves)
					print()
					#move = moves[randint(0,len(moves)-1)]
					#print(move)
					comp_choice = randint(1,9)
					#comp_choice = move[randint(0,len(moves)-1)]
					if comp_choice in taken_squares:
						continue
					else:
						b[valid_squares.get(comp_choice)[0]][valid_squares.get(comp_choice)[1]] = comp
						taken_squares.append(comp_choice)
						comp_squares.append(comp_choice)
						valid = 1	
	print_grid(b)
	print()
	if check_winner(user_squares,comp_squares)[1] == True: # Check for winner
		print(check_winner(user_squares,comp_squares)[0])
		winner = True
		break
	if len(taken_squares) == 9: # Terminate game if 9 moves have been taken without a winner
		print("Draw")
		break

	