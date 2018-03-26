# Introduction to Python

# Loop Control Statements

i = 1

while i <= 10:
    print(i)
    i += 1
    
# Break statement
    
i = 1

while i <= 10:
    if i > 5:
        #come out of this loop
        break
    print(i)
    i += 1
    
# Continue
    
i = 1

while i <= 10:
    if i >= 4 and i <= 7:
        i += 1
        continue
    print(i)
    i += 1
    
    
for i in range(1,11):
    if i >= 4 and i <= 7:
        continue
    print(i)
    
    
# Pass

i = 1

if i == 1:
    pass
else:
    pass