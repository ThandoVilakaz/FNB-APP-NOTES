fruit = ["apple","banana","cherry"]
print(fruit[0])

#lists are mutable(changeable)
fruit[1] = "blueberry"
print(fruit)

#adding/removing
#to add we use the appeand method
fruit.append("kiwi")
print(fruit)

#adding a value at a specific position
#use the insert method
fruit.insert(1,"orange")
print(fruit)

#use the remove method to remove an item
fruit.remove("kiwi")
print(fruit)

#sorting
fruit.sort() #ascending order
print(fruit)

#descending
fruit.sort(reverse=True)
print(fruit)
