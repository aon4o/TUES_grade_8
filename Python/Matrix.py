matrix=[[1,0,0,0,0,0],[1,1,0,0,0,0],[2,1,0,0,0,0],[0,1,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
w=True
w1=True

#def randomize():
#	for x in range(0,6):
#		for y in range(0,6):
#			matrix[y][x]=random(0,1)
#	matrix[random(0,5)][random(0,5)]=2
#randomize()

for z in range(0,len(matrix)):
	if 2 in matrix[z]:
		endX=(matrix[z].index(2))
		endY=(z)

class Player():
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def moveUp(self):
		if self.y-1 < 0:
			print("	You can't go there!!!\n")
		elif matrix[self.y-1][self.x]==0:
			self.y-=1
			print("	Your moved and your position now is --> "+"x="+str(self.x)+" y="+str(self.y)+".\n")
		elif matrix[self.y-1][self.x]==2:
			self.y-=1
			print("	You found the finish and you WIN!!!")
		else:
			print("	You can't go there!!!\n")
	def moveDown(self):
		if self.y+1 > len(matrix)-1:
			print("	You can't go there!!!\n")
		elif matrix[self.y+1][self.x]==0:
			self.y+=1
			print("	Your moved and your position now is --> "+"x="+str(self.x)+" y="+str(self.y)+".\n")
		elif matrix[self.y+1][self.x]==2:
			self.y+=1
			print("	You found the finish and you WIN!!!")
		else:
			print("	You can't go there!!!\n")
	def moveLeft(self):
		if self.x-1 < 0:
			print("	You can't go there!!!\n")
		elif matrix[self.y][self.x-1]==0:
			self.x-=1
			print("	Your moved and your position now is --> "+"x="+str(self.x)+" y="+str(self.y)+".\n")
		elif matrix[self.y][self.x-1]==2:
			self.x-=1
			print("	You found the finish and you WIN!!!")
		else:
			print("	You can't go there!!!\n")
	def moveRight(self):
		if self.x+1 > len(matrix[self.y])-1:
			print("	You can't go there!!!\n")
		elif matrix[self.y][self.x+1]==0:
			self.x+=1
			print("	Your moved and your position now is --> "+"x="+str(self.x)+" y="+str(self.y)+".\n")
		elif matrix[self.y][self.x+1]==2:
			self.x+=1
			print("	You found the finish and you WIN!!!")
		else:
			print("	You can't go there!!!\n")
	def prPos(self):
		print("	x="+str(self.x)+" y="+str(self.y)+" "+str(matrix[self.y][self.x])+"\n")
	def prMap(self):
		self.matrix=matrix
		self.matrix[self.y][self.x]=3
		for a in self.matrix:
			print(*a)
		self.matrix[self.y][self.x]=0
		print("The '0' are the places where you can step on.")
		print("The '1' are the places where you can't step on.")
		print("The '2' is the place where you win the game.")
		print("The '3' is the place where you are right now.\n")
	def x():
		return self.x
	def y():
		return self.y
	
while w:
	x=int(input("Type in your starting X position (from 0 to 5) --> "))
	y=int(input("Type in your starting Y position (from 0 to 5) --> "))
	if isinstance(x, int) and isinstance(y, int):
		if x>5 or x<0:
			print("	You can't start from this position!!!\n")
		elif y>5 or y<0:
			print("	You can't start from this position!!!\n")
		elif matrix[y][x]==1:
			print("	You can't start from this position!!!\n")
		elif matrix[y][x]==2:
			print("	You started from the winning position... and you WIN!?")
			w=False
		else:
			w=False
			player=Player(x,y)
			print("	Your start position is --> "+"x="+str(player.x)+" y="+str(player.y)+".")
			print("	The End is on position --> x="+str(endX)+" y="+str(endY)+".")
			print("	If you need help you can always type in 'help'.")
			while w1:
				a=str(input("Type here your command --> "))
				if a=="up" or a=="Up":
					player.moveUp()
					if matrix[player.y][player.x]==2:
						w1=False
				elif a=="down" or a=="Down":
					player.moveDown()
					if matrix[player.y][player.x]==2:
						w1=False
				elif a=="right" or a=="Right":
					player.moveRight()
					if matrix[player.y][player.x]==2:
						w1=False
				elif a=="left" or a=="Left":
					player.moveLeft()
					if matrix[player.y][player.x]==2:
						w1=False
				elif a=="break" or a=="exit":
					break
				elif a=="prPos" or a=="pos" or a=="position":
					player.prPos()
				elif a=="map" or a=="prMap":
					player.prMap()
				elif a=="help":
					print("	THIS IS THE LIST OF COMMANDS YOU CAN USE:\n	help: Shows you THIS!\n	up: Moves your player up on the Y coordinate.\n	down: Moves your player down on the Y coordinate.\n	left: Moves your player left on the X coordinate.\n	right: Moves your player right on the X coordinate.\n	exit: Closes the program.\n	position: Prints your coordinates in numbers.\n	map: Shows tou the map your playing on, your position and the goal.\n")
				#elif a=="random" or a=="randomize" or a=="restart" or a=="reset":
				#	randomize()
				else:
					print("	That's not a recognized command!!!\n")
	else:
		print("	Yoh have to put in NUMBERS!!!\n")
