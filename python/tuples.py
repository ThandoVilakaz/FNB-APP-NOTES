'''Tuples are ordered can't be changed once created unlike lists
Tuples can be used when you want to store a collection of elements 
that should not be changed e.g coordinates etc.'''
my_tuple = (1,2,3,4,5)
print(my_tuple)

#access just like the lists
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[-1]) #negative indexing

#operations with tuples
tuple1 = (1,2,3)
tuple2 = (4,5,6)
conc_tuple = tuple1 + tuple2 #concatinating
print(conc_tuple)

rep_tuple = tuple1 *3   #repeating
print(rep_tuple)


