# Introduction to Python

# Block of meaningful code

def functionName(arg1,arg2):
    print(arg1,arg2)
    
functionName('The number is',12)

def sumOfTwo(num1,num2):
    return (num1+num2)

print(sumOfTwo(12,15))


# Our own length function

def length(l):
    count = 0
    for item in l:
        count += 1
    return count

print(length([12,14,566]))