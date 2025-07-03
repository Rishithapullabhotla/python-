""" 
identity operators are used to compare the values 
and return the boolean values.. 
the operators are "is", "is not" 
""" 
x = [ 1,2,3] 
y = [ 4, 5,6] 
z = x 
print(x is y)#F 
print(x is z)#T 
print(y is z)#F 
print(y is not z)#T 
print(z is not x)#F 
print(x is not y)#T