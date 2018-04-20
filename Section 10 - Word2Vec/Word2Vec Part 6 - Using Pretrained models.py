# Word2Vec model visualization

# Install gensim - pip install gensim
from gensim.models import KeyedVectors

filename = 'GoogleNews-vectors-negative300.bin'

model = KeyedVectors.load_word2vec_format(filename, binary=True)

model.wv.most_similar('king')

model.wv.most_similar(positive=['king','woman'], negative= ['man'])