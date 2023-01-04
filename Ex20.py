import nltk
nltk.download()
from nltk.util import ngrams
file1 = open("Readme.txt")
samplText = file1.read()

NGRAMS = ngrams(sequence=nltk.word_tokenize(samplText), n=3)
for grams in NGRAMS:
    print(grams)