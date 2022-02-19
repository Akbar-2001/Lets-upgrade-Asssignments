# 1. Find the data type of a if a=9
# a=9
# print(a, "is of type", type(a))

# 9 is of type <class 'int'>

# ///////////////////////////////////////////////////////////#

# 3. Find the data type of a if a='9.'
# a='9.'
# print(a, "is of type", type(a))

# 9. is of type <class 'str'>

#///////////////////////////////////////////////////////////#

# 4. Find the data type of a if a=(9)
# a=(9)
# print(a, "is of type", type(a))

# 9 is of type <class 'int'>

#///////////////////////////////////////////////////////////#

# 5. Find the data type of a if a=False
# a=False
# print(a, "is of type", type(a))

# False is of type <class 'bool'>

#///////////////////////////////////////////////////////////#

# 6. Find the data type of a if a=[1,2,3]
# a=[1,2,3]
# print(a, "is of type", type(a))
# [1, 2, 3] is of type <class 'list'>

#///////////////////////////////////////////////////////////#

# 7. Find the data type of a if a=(1,2,3)
# a=(1,2,3)
# print(a, "is of type", type(a))
# (1, 2, 3) is of type <class 'tuple'>

#///////////////////////////////////////////////////////////#

# 8. Find the data type of a if a={'key': 9}
# a={'key': 9}
# print(a, "is of type", type(a))
# {'key': 9} is of type <class 'dict'>

#///////////////////////////////////////////////////////////#

# 9. Find the data type of a if a=1 + 9j
# a=1 + 9j
# print(a, "is of type", type(a))
# (1+9j) is of type <class 'complex'>

#///////////////////////////////////////////////////////////#

# 10. Set a=1 and b=2. What data type is a/b?
# a=1
# b=2
# print(a/b, "is of type", type(a/b))
# 0.5 is of type <class 'float'>

#///////////////////////////////////////////////////////////#

# 11. Create a dictionary numbers = {'one':1, 'two':2, 'three':3}. Pull out the number '2' by calling the key 'two'.
# Dict = {'one':1, 'two':2, 'three':3}
# print("creating Dictionary: ")
# print(Dict)

# del Dict['two']
# print("\nDeleting a key from Dictionary: ")
# print(Dict)

# creating Dictionary: 
# {'one': 1, 'two': 2, 'three': 3}

# Deleting a key from Dictionary:
# {'one': 1, 'three': 3}

#///////////////////////////////////////////////////////////#

# 12. Create a tuple with the numbers 8, 9, and 10?
# tuplex = 8, 9, 10
# print(tuplex)

# (8, 9, 10)

#///////////////////////////////////////////////////////////#

# 1. Run the following lines of code and explain the error in your own words. Then rewrite the lines of code to run error free:
# d = {one:1, two:2, three:3}
# d[one]

# explanation

# from the above code we are trying to create an dict but there is an 
# Nameerror in the code to over come we need to defined the name using
# single ('') code.

#executable code

# d = {'one':1, 'two':2, 'three':3}
# print(d['one'])

#///////////////////////////////////////////////////////////#

# 14. Run the following lines of code and explain the error in your own words. Then rewrite the lines of code to run error free:
# f = false not f

# f = str('false')
# print(f)

# explanation
# when we are going to declare a string we should need to call by its function.

#///////////////////////////////////////////////////////////#

# 1. Run the following lines of code and explain the error in your own words. Then rewrite the lines of code to run error free:
# lst = [1,3,5] lst[3]

# lst = [1,3,5] 
# print(lst)