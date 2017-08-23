import nltk
import sys


str='''I love to dance. I like to dance I. like to play chess.'''
#str=sys.stdin.read()

str=str.strip().lower().replace('\n',' ')

token=list(str.split(" "))
clean_str=[b for b in token if b.isalnum()]
trigram=list(nltk.trigrams(token))
print list(trigram)
fdist = nltk.FreqDist(word for word in trigram)
most_comm=fdist.most_common(1)
for mc in most_comm:
    print mc
