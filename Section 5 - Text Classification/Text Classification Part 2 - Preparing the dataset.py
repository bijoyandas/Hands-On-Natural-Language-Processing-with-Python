# Text Classifiation using NLP

# Importing the libraries
import numpy as np
import re
import pickle 
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# Importing the dataset
with open('test.ft.txt','r',encoding='utf8') as f:
    dataset = f.readlines()[:50000]

# Preparing the dataset
for i in range(len(dataset)):
    dataset[i] = re.sub(r'__label__1','0\t',dataset[i])
    dataset[i] = re.sub(r'__label__2','1\t',dataset[i])
    
X = []
y = []
for review in dataset:
    textandsent = review.split('\t')
    y.append(textandsent[0])
    X.append(textandsent[1])

y = [int(sent) for sent in y]