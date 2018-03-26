# Introduction to Python

# Structure of if statements
"""
if condition:
    Statements
elif condition:
    Statements
else:
    Statements
"""


#Grade of a student

marks = 90

# No braces in Python, Indectation does the job

if marks > 90:
    print("Grade O")
elif marks > 80:
    print("Grade E")
elif marks > 70:
    print("Grade A")
elif marks > 60:
    print("Grade B")
elif marks > 50:
    print("Grade C")
else:
    print("Better luck next time")

# Divisible or not

number1 = 45
number2 = 5

if number1%number2 == 0:
    print("Divisible")
else:
    print("not divisible")