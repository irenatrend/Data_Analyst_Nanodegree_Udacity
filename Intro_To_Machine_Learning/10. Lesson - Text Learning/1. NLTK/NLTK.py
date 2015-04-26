# Download nltk
# import nltk
# nltk.download()

from nltk.corpus import stopwords
sw = stopwords.words("english")

print sw[0]
print sw[5]
print sw[10]

# How many stopwords are there?
print "Number of stopwords:", len(sw)

# Stemming with NLTK
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

print stemmer.stem("responsiveness")
print stemmer.stem("responsivity")
print stemmer.stem("unresponsive")