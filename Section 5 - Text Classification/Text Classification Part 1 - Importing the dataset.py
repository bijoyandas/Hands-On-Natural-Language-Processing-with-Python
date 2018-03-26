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