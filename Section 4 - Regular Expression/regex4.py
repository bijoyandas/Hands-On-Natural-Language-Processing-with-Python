# Introduction to Python Regular Expressions

# Importing the libraries
import re

sentence1 = "Welcome to the year 2018"
sentence2 = "Just ~%* ++++--- arrived at @Jack's place. #fun"
sentence3 = "I                  love                u"

sentence1_modified = re.sub(r'\d','',sentence1)

sentence2_modified = re.sub(r'[@#\.\']','',sentence2)

sentence2_modified = re.sub(r'\W',' ',sentence2)

sentence2_modified = re.sub(r'\s+',' ',sentence2_modified)                               

sentence2_modified = re.sub(r"\s+[a-zA-Z]\s+",' ',sentence2_modified)

sentence3_modified = re.sub(r'\s+',' ',sentence3)                           