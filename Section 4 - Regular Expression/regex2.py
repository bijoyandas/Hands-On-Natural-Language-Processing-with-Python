# Introduction to Python Regular Expressions

# Importing Libraries
import re

pattern1 = "Apples are tasty"
pattern2 = "Today I feel like crying."

if re.match(r"^Apples",pattern1):
    print("Matches!")
else:
    print("No Match!")
    
if re.search(r"\.$",pattern2):
    print("Match!")
else:
    print("No Match!")