# Introduction to Python

# Console I/O

inp = input('Enter a number: ')
number1 = int(inp)

inp = input('Enter a number: ')
number2 = int(inp)

print(number1+number2)

# File I/O

# Writing to a file

inp = input('Enter some text: ')

with open('textFile.txt','a') as f:
    f.write(inp)
    
# Reading from a file
    
with open('textFile.txt','r') as f:
    string = f.read()
    print(string)