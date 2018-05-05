# Created by Bijoyan Das on 12/2/2018 at 12:33:43 PM
"""
Sentiment Analysis using TF-IDF model and Linear SVC

Data: 
50000 movie reviews from IMDB has been used in this model,
out of which 40000 reviews have been used to train and rest of the
10000 reviews have been used to test the model performance.

Preprocessing:
Preprocessing stage consists of removing non-character symbols, 
adding 'not_' before the word where there's an occurence of 'not' etc.
The preprocessed data is stored in corpus.

Model:
Here I have used TfidfVectorizer from sklearn.feature_extraction.text
library which works similarly to CounterVectorizer followed by
TfidfTransformer. Due to this we can assign different weights to words,
and all words are not given the same importance.

Machine Learning:
There are 2000 features used in this model and because of that
LinearSVC works the best for predicting sentiments with a accuracy of
89.80%. This model is also tested with other learning algorithms like
MultinomialNB, RandomForest with 500 estimators and LinearSVC out-performs
all of them.

Cross Validation:
We have used 10 fold cross validation on this model to determine the
accuracy of the model on different datasets and we get a mean of 89.80%
from all the 10 results.

Complete list of Accuracies per max_feature value:
1000 86.50%
2000 88.27%
3000 88.87%
4000 89.17%
5000 89.28%
6000 89.42%
7000 89.61%
8000 89.62%
9000 89.74%
10000 89.74%
12000 89.80%
"""

# Importing the libraries
import numpy as np
import re
import pickle 
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


# Importing the dataset
from sklearn.datasets import load_files
reviews_train = load_files('train/')
reviews_test = load_files('test/')
X_train,y_train = reviews_train.data,reviews_train.target
X_test,y_test = reviews_test.data,reviews_test.target
X = X_train + X_test
y = np.concatenate([y_train,y_test])
X = X[:50000]
y = y[:50000]


# Unpickling dataset
X_in = open('X.pickle','rb')
y_in = open('y.pickle','rb')
X = pickle.load(X_in)
y = pickle.load(y_in)


# Improving the stop words list
stop_words = stopwords.words('english')
uncheck_words = ['don','won','doesn','couldn','isn','wasn','wouldn','can','ain','shouldn','not']


# Creating the corpus which is the input to TfidfVectorizer
corpus = []
for i in range(0, len(X)):
    antonyms = []
    review = re.sub(r'\W', ' ', str(X[i]))
    review = re.sub(r'\d', ' ', review)
    review = review.lower()
    review = re.sub(r'br[\s$]', ' ', review)
    review = re.sub(r'\s+[a-z][\s$]', ' ',review)
    review = re.sub(r'b\s+', '', review)
    review = re.sub(r'\s+', ' ', review)
    word_list = review.split(' ')
    newword_list = []
    temp_word = ''
    for word in word_list:
        if temp_word in uncheck_words:
            if word not in stop_words:
                word = 'not_' + word
                temp_word = ''
        if word in uncheck_words:
            temp_word = word
        if word not in uncheck_words:
            newword_list.append(word)
    review = ' '.join(newword_list)
    corpus.append(review)    

# Creating the weighted BOW model using TF-IDF methodology
from sklearn.feature_extraction.text import TfidfVectorizer
tiv = TfidfVectorizer(max_features = 8000, min_df = 2, norm="l2", use_idf=True, sublinear_tf = True, max_df = 0.6, stop_words = stop_words)
X = tiv.fit_transform(corpus).toarray()


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
text_train, text_test, sent_train, sent_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Fitting the Training set to Linear SVC
from sklearn.svm import LinearSVC
classifier = LinearSVC(C = 0.1)
classifier.fit(text_train,sent_train)


from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB()
classifier.fit(text_train,sent_train)

# Fitting Random Forest Classification to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
classifier.fit(text_train, sent_train)


# Pickling classifier
with open('svcclassifier.pickle','wb') as f:
    pickle.dump(classifier,f)
    

# Pikling TF-IDF model
with open('TFIDF.pickle','wb') as f:
    pickle.dump(tiv,f)    


# Predicting the Test set results
sent_pred = classifier.predict(text_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(sent_test, sent_pred)

print(cm[0][0]+cm[1][1])

# Applying k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = text_train, y = sent_train, cv = 10)
accuracies.mean()
accuracies.std()