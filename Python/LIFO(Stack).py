class Stack:
	def __init__(self, size):
		self.size=size
		self.list=list(range(self.size))
		self.index=0
	def push(self,num):
		if self.index==self.size:
			print("You can't add more numbers!!!")
		else:
			self.list[self.index]=num
			self.index+=1
			print("You added the number --> "+str(num))
	def pop(self):
		if self.index==0:
			print("There's nothing left for you to take out!!!")
		else:
			self.index-=1
			print("The number you popped in --> "+str(self.list[self.index]))
			self.list[self.index]="none"
	def pr(self,num):
		if num-1>=self.size or num-1<0:
			print("You can't print unreal thing!!!")
		elif self.list[num-1]=="none":
			print("This index isn't occupied yet!!!")
		else:	
			print(self.list[num-1])
	
	
	
			
a=Stack(5)
a.push(2)
a.push(3)
a.push(5)
a.push(7)
a.push(9)
a.push(12)

a.pr(3)
a.pr(5)
a.pr(6)

a.pop()
a.pop()
a.pop()
a.pop()
a.pop()
a.pop()

a.pr(-4)
a.pr(3)
a.pr(4)