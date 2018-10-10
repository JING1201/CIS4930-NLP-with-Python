'''
Name		Jing Low
Section	27F3
Assignment	03
Due Date	January 31, 2018
'''
import nltk
from nltk.corpus import state_union as su
from nltk.corpus import wordnet as wn
from nltk.corpus import brown

def problem_1():
    su_freq = nltk.ConditionalFreqDist(
	            (word, fileid[:4])
	            for fileid in su.fileids()
	            for word in su.words(fileid) if word in ['men','women','people'])
    su_freq.plot()

def problem_2():
    count = 0
    for synset in wn.all_synsets('n'):
        if len(synset.hyponyms())==0:
            count+=1
    print(count/len(list(wn.all_synsets('n')))*100)

def problem_3():
    #adjectives
    primary_emotions = ['happy','sad','angry','scared']
    cfd = nltk.ConditionalFreqDist(
	        (genre, word)
	        for genre in brown.categories()
	        for word in brown.words(categories=genre) if word in primary_emotions)
    cfd.tabulate()
    #nouns
    primary_emotions = ['joy','sadness','anger','fear']
    cfd = nltk.ConditionalFreqDist(
	        (genre, word)
	        for genre in brown.categories()
	        for word in brown.words(categories=genre) if word in primary_emotions)
    cfd.tabulate()

#problem_4
def censor (bad_words, better_words, text):
    words = text.split()
    ans = ''
    for word in words:
        if word in bad_words:
            word = better_words[bad_words.index(word)]
        ans += word+" "
    return ans.strip()