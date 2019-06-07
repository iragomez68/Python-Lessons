#Create a variable set it as a list
myList = ["Jack", 24, "Donald", 80]
print(myList)

myList.append("Bob")
print(myList)

#Change 4th element from 80 to 93
myList[3] =93

#Remove Bob from list
myList.remove("Bob")
print(myList)

#Remove first element
myList.pop(0)
print(myList)

#Tuples, cannot add, remove or modify a tuple
myTuple = ('Python', 80, 'VBA', False)
print(myTuple)