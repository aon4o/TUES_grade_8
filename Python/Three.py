class Leaf():
	def __init__(self,value,dad):
		self.value=value
		self.dad=dad
		self.list=list()
		
	def addKid (self,value,dad):
		child = Leaf(self.value,dad)
		self.list.append(child)
		return child
		
	def __str__(self):
		pass
		#return "Leaf(" + str(self.value) +") " + "".join([str(x) for x in self.list])
	
	
	
kur=Leaf(23,None)
kur.addKid(23,kur)
kur.addKid(14,367)
