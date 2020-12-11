def bubbleSort(list):
	for num in range(0,len(list)-1):
		for index in range(0,len(list)-1-num):
			if list[index]>list[index+1]:
				list[index],list[index+1]=list[index+1],list[index]
				#за размяната на местата на двете числа
				#може да се използва и:
				#temp=list[index]
				#list[index]=list[index+1]
				#list[index+1]=temp

myList=[5,1,7,3]
bubbleSort(myList)
print(myList)