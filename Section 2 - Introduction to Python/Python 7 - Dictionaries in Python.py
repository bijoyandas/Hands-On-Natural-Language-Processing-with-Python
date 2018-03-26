# Introduction in Python

# Key - Value Pairs

dict1 = {}

# Adding elements to the dictinary

dict1['apple'] = 'Apple is a fruit'
dict1['orange'] = 'Orange is a fruit'
dict1['car'] = 'Cars are fast'
dict1['python'] = 'Python is a snake'

# Printing dictionary elements

print(dict1)
print(dict1['apple'])
print(dict1['car'])
print(dict1['python'])

print(dict1.get('jython','Does not exist'))

# Deleting elements

del dict1['apple']

# Length of a dictionary

print(len(dict1))

# List of keys and Values

listOfKeys = list(dict1.keys())
listOfValues = list(dict1.values())

# Looping through lists

for key in dict1.keys():
    print(dict1[key])