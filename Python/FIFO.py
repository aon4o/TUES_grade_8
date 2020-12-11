class FIFO
	def __init__(self, size):
		self.size=size
		self.list=list(range(size))
		self.indexE=0
		self.indexD=0
	def enqueue(self, num)
		if self.indexE==self.size
			print("You can't add more to this list!!!")
		else:
			self.list[self.indexE]=num
			print("You added this number --> "+str(num))
			self.indexE+=1
	def dequeue(self):
		if self.indexD==self.size:
			print("There's nothing more to be removed!!!")
		else:
			print("You deleted this number --> "+ str(self.list[self.indexD]))
			self.list[self.indexD]="none"
			self.indexD+=1
	def pr(self, num):
		if num-1<0 or num>self.size:
			print("You can't print thing that isn't there!!!")
		else:
			print(self.list[num-1])