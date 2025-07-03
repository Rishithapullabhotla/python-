mylist=[1,2,3,45,67,89,567.8,56]
print(mylist)
print(mylist[5])
print(mylist[-4])
#append method
#syntax = list variablename.method()
#append method is used to add the elements at the end of the list
fruits=[12, "goa,","sapota"]
print(fruits)
fruits.append("apple")
print(fruits)
#extend
fruits.extend(["hello","edinburgh","UK"])
print(fruits)
#count used to tell about the repeated items in  a list
flowers=["rose","marie gold","rose"]
print(flowers.count("rose"))
#mutabbility
mylist3=[12,33,44,55,66]
print(mylist3)
mylist3[2]="hello"
print(mylist3)
#pop-- removes the element using a index 
list5=[12,34,67,89,90]
print(list5.pop(2))
#mutability--changing the elements
mylist4=["hello","ece",123,34.56,56+78j]
print(mylist4)
mylist4[2]="agri"
print(mylist4)
#pop--removes the elements using index
mylist5=[12,34,565,78.9,34+56j,"hello"]
print(mylist5)
mylist5.pop(2)
print(mylist5)
#remove--removes the element directly
#that are present in a list
mylist5.remove(34)
print(mylist5)
#count--it counts the number of occurance
#of a item in a list
mylist6=[22,33,33,22,55,22,44,67,56,22]
print(mylist6.count(22))
"""
Note:It will take almost only one arguement
""" 
#insert--it just inserts the elements into the list
#using the index
mylist7=[22,33,44,77,88]
print(mylist7)
mylist7.insert(1,"hello")
print(mylist7)
"Note:In insert method no element is removed"
"they just replaces the position"
""
#index--this method tells the position of a element
#it tells the first occurance when an element is repeated
mylist8=[22,44,55,55,44,66,67,89]
print(mylist8.index(44))#1
print(mylist8.index(55))#2
#reverse--it just reverses the elements
mylist8.reverse()
print(mylist8)
#copy--it just copy the elements in a list
mylist9=[22,33,44,55,66,77]
mylist
