# Latent Semantic Analysis using Python

# Importing the Libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

# Sample Data
dataset = ["The amount of polution is increasing day by day",
           "The concert was just great",
           "I love to see Gordon Ramsay cook",
           "Google is introducing a new technology",
           "AI Robots are examples of great technology present today",
           "All of us were singing in the concert",
           "We have launch campaigns to stop pollution and global warming"]

dataset = [line.lower() for line in dataset]

# Creating Tfidf Model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset)

# Visualizing the Tfidf Model
print(X[0])


# Creating the SVD
lsa = TruncatedSVD(n_components = 4, n_iter = 100)
lsa.fit(X)


# First Column of V
row1 = lsa.components_[3]


# Visualizing the concepts
terms = vectorizer.get_feature_names()
for i,comp in enumerate(lsa.components_):
    componentTerms = zip(terms,comp)
    sortedTerms = sorted(componentTerms,key=lambda x:x[1],reverse=True)
    sortedTerms = sortedTerms[:10]
    print("\nConcept",i,":")
    for term in sortedTerms:
        print(term)