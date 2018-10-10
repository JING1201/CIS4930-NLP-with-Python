#analysis_content

import nltk
from nltk.book import *
from nltk.corpus import stopwords

def problem_1():
    #answer in code format
    all = []
    for i in range (1,len(text6)):
        if text6[i].isalpha() and (text6[i-1].lower()=='knight' or text6[i-1].lower() == 'sir' ):
            if text6[i].lower() != 'knight' and text6[i][0].isupper() and text6[i].lower() not in stopwords.words("english"):
                all.append(text6[i])
    fqd = nltk.FreqDist([word.lower() for word in all])
    print ("Name of knights", list(set([word.lower() for word in all])))
    print("Most Common: ",fqd.max())

def problem_2():
    entries = nltk.corpus.cmudict.entries()
    #print("check")
    words = []
    repeated = []
    count = 0
    for word, pron in entries:
        #print(word)
        #print(pron)
        if word not in words:
            words.append(word)
        elif word not in repeated:
            repeated.append(word)
    print ("Number of distinct words: ", len(words))
    print ("Fraction of words that have more than one possible pronunciation: ", (len(repeated)/len(words)))

def problem_3(text):
    words = text.split()
    fqd = nltk.FreqDist([word for word in words if word.isalpha() and word not in stopwords.words("english")
            and word in nltk.corpus.words.words()])
    if len(list(fqd)) < 50:
        print (fqd.most_common())
    else:
        print (fqd.most_common(50))

def problem_4(text):
    words = text.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    print (text)
    print (acronym)
    return acronym

def main():
    problem_1()
    problem_2()
    text = input ("Please input text: ")
    problem_3(text)
    text = input ("Please input text")
    problem_4(text)