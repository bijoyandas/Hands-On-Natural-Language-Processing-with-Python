# Introduction to Python Regular Expressions

# Importing Libraries
import re

pattern1 = "abcd"
pattern1 = "9876 efg 98"
pattern1 = "a"

print("Occurences of any character: ",re.match(r".+",pattern1))
print("Occurences of A_Za-z: ",re.search(r"[a-z]+",pattern1))
print("Occurences of ab*: ",re.search(r"ab?",pattern1))

if re.match(r"[a-z]+",pattern1) != None:
    print("Match!")
else:
    print("No Match!")