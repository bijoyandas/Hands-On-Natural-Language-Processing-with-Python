# Text Classifiation using NLP

# Importing the libraries
import numpy as np
import re
import pickle 
import nltk
from nltk.corpus import stopwords
from sklearn.datasets import load_files
nltk.download('stopwords')


# Importing the dataset
reviews = load_files('txt_sentoken/')
X,y = reviews.data,reviews.target