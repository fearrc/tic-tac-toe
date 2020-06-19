from random import randint,choice
from tkinter import *

# Begin App Class
class App:
	def __init__(self):
		self.canvas= Canvas(root, width=90, height=90)
		self.top = 30
		self.bottom = 60
		self.left = 5
		self.right = 85
		self.canvas.create_line(self.top,self.left,self.top,self.right)
		self.canvas.create_line(self.bottom,self.left,self.bottom,self.right)
		self.canvas.create_line(self.left,self.top,self.right,self.top)
		self.canvas.create_line(self.left,self.bottom,self.right,self.bottom)

		self.canvas.focus_set()
		self.canvas.bind("<Button-1>", self.callback)
		self.canvas.pack()

		self.taken_squares = []
		self.user_squares = []
		self.comp_squares = []

		self.score = [0,0,0]
		self.winner = 0
		self.plays_first = randint(0,1)

		if self.plays_first == 0:
			self.player = 0
			self.user = "X"
			self.comp = "O"
		else:
			self.player = 1
			self.user = "O"
			self.comp = "X"
			self.find_best_move()

	def callback(self,event):
		if self.player == 0 and self.winner == 0:
			if event.x < self.top:
				if event.y < self.top:
					self.canvas.create_text((self.top+self.left)/2,(self.top+self.left)/2,text = self.user)
					self.canvas.pack()
					self.logic(1)
				elif event.y < self.bottom and event.y > self.top:
					self.canvas.create_text((self.top+self.left)/2,(self.bottom+self.top)/2,text=self.user)
					self.canvas.pack()
					self.logic(4)
				else:
					self.canvas.create_text((self.top+self.left)/2,(self.bottom+self.right)/2,text=self.user)
					self.canvas.pack()
					self.logic(7)
			elif event.x < self.bottom and event.x > self.top:
				if event.y < self.top:
					self.canvas.create_text((self.bottom+self.top)/2,(self.top+self.left)/2,text=self.user)
					self.canvas.pack()
					self.logic(2)
				elif event.y < self.bottom and event.y > self.top:
					self.canvas.create_text((self.bottom+self.top)/2,(self.bottom+self.top)/2,text=self.user)
					self.canvas.pack()
					self.logic(5)
				else:
					self.canvas.create_text((self.bottom+self.top)/2,(self.bottom+self.right)/2,text=self.user)
					self.canvas.pack()
					self.logic(8)
			else:
				if event.y < self.top:
					self.canvas.create_text((self.bottom+self.right)/2,(self.top+self.left)/2,text=self.user)
					self.canvas.pack()
					self.logic(3)
				elif event.y < self.bottom and event.y > self.top:
					self.canvas.create_text((self.bottom+self.right)/2,(self.bottom+self.top)/2,text=self.user)
					self.canvas.pack()
					self.logic(6)
				else:
					self.canvas.create_text((self.bottom+self.right)/2,(self.bottom+self.right)/2,text=self.user)
					self.canvas.pack()
					self.logic(9)

	def logic(self,selection):
		if self.player == 0:
			self.user_squares.append(selection)
		else:
			self.comp_squares.append(selection)
		self.taken_squares.append(selection)
		self.check_winner()

	# Function to determine if a winning configuration has ocurred
	def check_winner(self):
		if self.winner == 0:
			wins = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,5,7],[3,6,9],[4,5,6],[7,8,9]]
			for win in wins:
				if all(item in self.user_squares for item in win):
					x = Label(root, text = "user wins")
					x.pack()
					self.winner = 1
					break
				elif all(item in self.comp_squares for item in win):
					x = Label(root, text = "computer wins")
					x.pack()
					self.winner = 1
					break
				elif len(self.user_squares)+len(self.comp_squares)==9:
					x = Label(root, text = "draw")
					x.pack()
					self.winner = 1
					break
			if len(self.user_squares)+len(self.comp_squares)<9:
				if self.player == 0:
					self.player = 1
					self.find_best_move()
				else:
					self.player = 0

	def find_best_move(self):
		if self.player == 1 and self.winner == 0:
			freq = [5,1,3,7,9,2,4,6,8] 			# which cells are contained within the most winning configs
			for each in self.user_squares+self.comp_squares:
				freq.remove(each)
			wins = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,5,7],[3,6,9],[4,5,6],[7,8,9]]
			in_comp = []
			in_comp_only = []
			user_only = []
			for win in wins:
				u = [i for i in win if i in self.user_squares]
				c = [i for i in win if i in self.comp_squares]		# get list of values in winning config for the comp
				if len(u) == 2 and len(c) != 2: 					# if length of list is 2 then the user is one move away from a win
					what = list(set(win).difference(set(self.user_squares).union(set(self.comp_squares)))) 	# determine this value
					if what not in self.comp_squares and len(what) > 0:
						self.fill_square(what.pop())							# block the user by playing this value
				elif len(c) == 2:
					some = list(set(win).difference(set(self.user_squares).union(set(self.comp_squares))))
					if some not in self.user_squares and len(some) > 0:
						self.fill_square(some.pop())
				if any(item in self.comp_squares for item in win):
					in_comp.append(win)
					if all((item not in self.user_squares) for item in win):
						in_comp_only.append(win)
			if len(in_comp_only) != 0:
				for f in freq:
					for each in in_comp_only:
						for val in each:
							if val == f:
								self.fill_square(val)
								
			else:
				available = list(set(list(range(1,9))).difference(set(self.user_squares)))
				for f in freq:
					if f in available:
						self.fill_square(f)

	def fill_square(self,selection):
		if self.player == 1:
			if selection == 1:
				self.canvas.create_text((self.top+self.left)/2,(self.top+self.left)/2,text = self.comp)
				self.canvas.pack()
				self.logic(1)
			elif selection == 4:
				self.canvas.create_text((self.top+self.left)/2,(self.bottom+self.top)/2,text=self.comp)
				self.canvas.pack()
				self.logic(4)
			elif selection == 7:
				self.canvas.create_text((self.top+self.left)/2,(self.bottom+self.right)/2,text=self.comp)
				self.canvas.pack()
				self.logic(7)
			if selection == 2:
				self.canvas.create_text((self.bottom+self.top)/2,(self.top+self.left)/2,text=self.comp)
				self.canvas.pack()
				self.logic(2)
			elif selection == 5:
				self.canvas.create_text((self.bottom+self.top)/2,(self.bottom+self.top)/2,text=self.comp)
				self.canvas.pack()
				self.logic(5)
			elif selection == 8:
				self.canvas.create_text((self.bottom+self.top)/2,(self.bottom+self.right)/2,text=self.comp)
				self.canvas.pack()
				self.logic(8)
			elif selection == 3:
				self.canvas.create_text((self.bottom+self.right)/2,(self.top+self.left)/2,text=self.comp)
				self.canvas.pack()
				self.logic(3)
			elif selection == 6:
				self.canvas.create_text((self.bottom+self.right)/2,(self.bottom+self.top)/2,text=self.comp)
				self.canvas.pack()
				self.logic(6)
			elif selection == 9:
				self.canvas.create_text((self.bottom+self.right)/2,(self.bottom+self.right)/2,text=self.comp)
				self.canvas.pack()
				self.logic(9)

root = Tk()
app = App()
root.mainloop()
# End App Class