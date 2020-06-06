from random import randint
# Initialize Game Board
print("Tic Tac Toe \n")
def print_grid(grid):
    for row in grid:
        print(row)

def check_winner(user,comp):
	wins = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,5,7],[3,6,9],[4,5,6],[7,8,9]]
	for win in wins:
		if all(item in user for item in win):
			return "user wins",True
		elif all(item in comp for item in win):
			return "computer wins",True
	return "no winner",False


b = [[0,0,0],
	[0,0,0],
	[0,0,0]]

print_grid(b)
print()

while True:
    try:
        user = input('Choose x or o ')
        assert len(user) < 2 and type(user) == str
    except AssertionError:
        print("Invalid! Please enter x or o")
    else:
        break

if user == "x" or "X":
	comp = "o"
else:
	comp = "x" 

valid_squares = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}
taken_squares = []
user_squares = []
comp_squares = []
winner = False
while len(taken_squares) <= 8 or winner == False:
	user_choice = input("Pick Row and Column (r,c) ")
	user_choice = user_choice.split(",")
	user_choice = [int(user_choice[0])-1,int(user_choice[1])-1]
	#print(user_choice)
	
	for key in valid_squares.keys():
		#print(key)
		#print(valid_squares.get(key))
		if valid_squares.get(key) == user_choice:
			if key in taken_squares:
				print("That square is already taken")
				continue
			else:
				taken_squares.append(key)
				user_squares.append(key)

				#print(taken_squares)
				print()
	
				b[user_choice[0]][user_choice[1]] = user

				if len(taken_squares) > 8:
					break
				valid = 0
				while not valid:
					comp_choice = randint(1,9)
					#print(comp_choice)

					if comp_choice in taken_squares:
						continue
					else:
						b[valid_squares.get(comp_choice)[0]][valid_squares.get(comp_choice)[1]] = comp
						#turns += 1
						taken_squares.append(comp_choice)
						comp_squares.append(comp_choice)
						valid = 1	
	print_grid(b)
	#print()
	#print(taken_squares)
	print()
	if check_winner(user_squares,comp_squares)[1] == True:
		print(check_winner(user_squares,comp_squares)[0])
		winner = True
		break
	if len(taken_squares) == 9:
		print("Draw")
		break