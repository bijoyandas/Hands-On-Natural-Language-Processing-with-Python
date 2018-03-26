# Introduction to Python

# Two types of loops in Python

# While Loop

"""
while condition:
    Statements
"""

i = 1;

while i <= 10:
    print(i)
    i += 1
    
# For loop
    
for i in range(1,11):
    print(i)
    
# Nested Loops

"""
12345
12345
12345
12345
"""

for i in range(1,5):
    for j in range(1,6):
        print(j,end=" ")
    print()
    
    