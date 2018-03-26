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


# Pickling the dataset
with open('X.pickle','wb') as f:
    pickle.dump(X,f)
    
with open('y.pickle','wb') as f:
    pickle.dump(y,f)

# Unpickling dataset
X_in = open('X.pickle','rb')
y_in = open('y.pickle','rb')
X = pickle.load(X_in)
y = pickle.load(y_in)


# Creating the corpus
corpus = []
for i in range(0, 50000):
    review = re.sub(r'\W', ' ', str(X[i]))
    review = review.lower()
    review = re.sub(r'^br$', ' ', review)
    review = re.sub(r'\s+br\s+',' ',review)
    review = re.sub(r'\s+[a-z]\s+', ' ',review)
    review = re.sub(r'^b\s+', '', review)
    review = re.sub(r'\s+', ' ', review)
    corpus.append(review)    