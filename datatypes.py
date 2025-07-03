""""
Datatype tells about the type of data that a variable is holding on
datatypes are categorised into "5" types
1. Number
2. Sequence
3. Boolean
4. Set
5.Dictionary
"""
#Number -- which tells about the number datatypes divided into "3"types
""""
Integer-- which holds all the positive and negative whole numbers i.e 0 to n and 0 to -n
Integer can be represented as int()
"""

a = 123
print(a)
print(type(a))
print(id(a))

""""
type()-- which tells about the type of a value that internally compiler holding on
id ()-- which tells about the address location of a value
"""

a1=-90
print(a1)
print(type(a1))
print(id(a1))


"""
Float -- which holds all the decimal or fractional values i.e o to n.n and 0 to -n.n
it can be represented as Float()
"""

b = 89.456
print(b)
print(type(b))
print(id(b))

b1 = -78.67
print(b1)
print(type(b1))
print(id(b1))


"""
complex datatypes are used to hold the real and imaginary values
which can be represented as a+bj
"""
c = 78+67j
print(c)
print(type(c))
print(id(c))

c1 = -456+78j
print(c1)
print(type(c1))
print(id(c1))


""""
sequence datatypes are divided into "3" types
1. String
2. List
3. Tuple
"""
"""
String : It is a collection of / group of characters
It can be enclosed using the single quotes or double quotes
"""
a = "ists"
print(a)
print(type(a))
print(id(a))

d = 'ists'
print(d)
print(type(d))
print(id(d))
"""
List : It is a collection of items/values/elements
syntax : listname = [ val1, val2, ...valn]
"""

mylist = [23, 45.67, 56+89j, "hello"]#items/values/elements=4
print(mylist)
print(type(mylist))
print(id(mylist))
print(mylist[2])
print(mylist[3])

"""
in order to acess the elements individually we use indexing
indexing always starts with "0" ends with n-1
syntax to acess the elements
print(listname[elementposition])
"""

""""
Tuple is a collection of items/values / elements
syntax : Tuplename = (val1, val2, ....valn)
"""
mytuple=(12, 23.67, "hi", [1,2,3],(56,78,89))
print(mytuple)
print(type(mytuple))
print(id(mytuple))
print(mytuple[3])
"""
Giving a list within a list is called sublist
Giving a tuple within a tuple is called subtuple
"""


"""
Boolean : Boolean means checks the condition
they are divided to two ways 1. True 2. False
it can be represented as bool
"""
a = True
print(a)
print(type(a))

b = False
print(b)
print(type(b))


"""
Set : It is a collection of values/items/elements
syntax :setname= {val1, val2...valn}
A set cant accept the list..
"""
myset={12, 23.34, 56+78j, "hi",  (45, "hello"), True}
print(myset)
print(type(myset))

""""
Dictionary : It is a collection of key value Pairs
syntax : dictionaryname={key1:val1, key2:val2,..keyn:valn}
"""
mydict={1:"ists", "branch":"ece","location":"rjy"}
print(mydict)
print(type(mydict))