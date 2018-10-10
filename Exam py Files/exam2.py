'''
Name: Jing Low
Exam 2
Date: 2/23/2018
'''

import nltk
import re
from nltk.corpus import names

def T9convert(n):
    if n==2:
        return "[abc]"
    elif n==3:
        return "[def]"
    elif n==4:
        return "[ghi]"
    elif n==5:
        return "[jkl]"
    elif n==6:
        return "[mno]"
    elif n==7:
        return "[pqrs]"
    elif n==8:
        return "[tuv]"
    elif n==9:
        return "[wxyz]"
    else:
        return ""

def T9convertString(string):
    expression = ""
    for c in string:
        expression += T9convert(int(c))
    return expression

def digit_name(number):
    
    male_names = names.words('male.txt')
    female_names = names.words('female.txt')
    
    numString = str(number)
    numString = numString.replace("-","")
    pattern = "^"+T9convertString(numString)+"$"
    
    matches = [w for w in male_names if re.search(pattern, w, re.IGNORECASE)]
    matches += [w for w in female_names if re.search(pattern,w, re.IGNORECASE)]
    
    return matches

def corpus_crypto(corpus_string, string_to_encrypt):
    #I previously mistyped corpus_processed as corpus_proccessed
    corpus_processed = "".join([c for c in corpus_string if c.isalpha()])
    string_processed = "".join([c for c in string_to_encrypt if c.isalpha()])
    corpus_fd = nltk.FreqDist(corpus_processed)
    corpus_c_ordered = [v[0] for v in corpus_fd.most_common()]
    string_fd = nltk.FreqDist(string_processed)
    #I previously mistyped string_fd below as string_processed
    string_c_ordered = [v[0] for v in string_fd.most_common()]
    
    ans = ""
    for c in string_to_encrypt:
        if not c.isalpha():
            ans += c
        else:
            ans += corpus_c_ordered[string_c_ordered.index(c)]
    
    return ans

def file_search(filename, word):
    
    f = open(filename, 'r')
    words = []
    for line in f:
        words += [w.lower() for w in re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", line) if w[0].isalpha()]
    f.close()
    
    print(words)
    
    same_length_words = [w for w in words if len(w) == len(word)]
    
    fd = nltk.FreqDist(words)
    
    word_freq = fd[word.lower()]
    all_freq = len(same_length_words)
    
    lexical_diversity = word_freq/all_freq
    
    return lexical_diversity

def main():
    num = input("Input for problem 1: ")
    digit_name(num)
    corp = input ("Input corpus for problem 2: ")
    encryp = input ("Input string to encrypt for problem 2: ")
    corpus_crypto(corp, encryp)
    path = input ("Input path to file for problem 3: ")
    word = input ("Input word to search for in problem 3: ")
    file_search(path, word)

