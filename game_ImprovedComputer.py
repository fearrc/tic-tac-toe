from random import randint,choice
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
	freq = [5,1,3,7,9,2,4,6,8] # which cells are contained within the most winning configs
	for each in user+comp:
		freq.remove(each)
	wins = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,5,7],[3,6,9],[4,5,6],[7,8,9]]
	in_comp = []
	in_comp_only = []
	user_only = []
	for win in wins:
		u = [i for i in win if i in user]
		c = [i for i in win if i in comp]										# get list of values in winning config for the comp
		if len(u) == 2 and len(c) != 2: 					# if length of list is 2 then the user is one move away from a win
			what = list(set(win).difference(set(user).union(set(comp)))) 	# determine this value
			if what not in comp and len(what) > 0:
				return what.pop()							# block the user by playing this value
		elif len(c) == 2:
			some = list(set(win).difference(set(user).union(set(comp))))
			if some not in user and len(some) > 0:
				return some.pop()
		if any(item in comp for item in win):
			in_comp.append(win)
			if all((item not in user) for item in win):
				in_comp_only.append(win)
	if len(in_comp_only) != 0:
		for f in freq:
			for each in in_comp_only:
				for val in each:
					if val == f:
						return val
	else:
		available = list(set(list(range(1,9))).difference(set(user)))
		for f in freq:
			if f in available:
				return f
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
if user == "x" or user == "X":
	comp = "o"
else:
	comp = "x" 
# Initialize dictionaries and lists that track possible moves and already made moves
valid_squares = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}
taken_squares = []
user_squares = []
comp_squares = []
winner = False
while len(taken_squares) <= 8 and winner == False:
	user_choice = input("Pick Row and Column (r,c) ")
	user_choice = user_choice.split(",")
	user_choice = [int(user_choice[0])-1,int(user_choice[1])-1]
	
	if check_winner(user_squares,comp_squares)[1] == True: # Check for winner
		print(check_winner(user_squares,comp_squares)[0])
		winner = True
		break
	elif len(taken_squares) == 9: # Terminate game if 9 moves have been taken without a winner
		print("Draw")
		break

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
					comp_choice = find_best_move(user_squares,comp_squares)
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