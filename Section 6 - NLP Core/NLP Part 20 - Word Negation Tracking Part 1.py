# Word Negation Tracking - Strategy 1

import nltk

sentence = "I was not happy with the team's performance"

words = nltk.word_tokenize(sentence)

new_words = []

temp_word = ''
for word in words:
    if word == 'not':
        temp_word = 'not_'
    elif temp_word == 'not_':
        word = temp_word + word
        temp_word = ''
    if word != 'not':
        new_words.append(word)

sentence = ' '.join(new_words)