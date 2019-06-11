# to assign any string to any existing function
# we are using strings later we'll use the eval() function to convert to function
sum([1, 2, 3])
mystring = 'sum'
myfun = eval(mystring)
print(myfun([1, 2, 3]))
