'''
Name		Jing Low
Section	    27F3
Assignment	Extra Credit 01
Due Date	March 19, 2018
'''

import nltk
from nltk import bigrams

def chi_square(w1, w2, corpus): 

    corpus_text = [w.lower() for w in corpus.words()]
    N = len(corpus_text)
    fdist_words = nltk.FreqDist(corpus_text)
    c_w1 = fdist_words[w1] 
    c_w2 = fdist_words[w2] 

    corpus_bigrams = list(bigrams(corpus_text))
    fdist_bigrams = nltk.FreqDist(corpus_bigrams)
    c_w1w2 = fdist_bigrams[(w1, w2)] 

    w1w2 = c_w1w2
    w1nw2 = c_w1 - c_w1w2
    w2nw1 = c_w2 - c_w1w2
    nw1nw2 = len(corpus_bigrams) - w1w2 - w1nw2 - w2nw1

    square  = [[w1w2, w1nw2],[w2nw1,nw1nw2]]

    E_i = []
    E_j = []
    E_temp1 = 0
    E_temp2 = 0
    for i in range (0, len(square)):
        E_temp1 = 0
        E_temp2 = 0
        for j in range (0, len(square[i])):
            E_temp1 += square[i][j]
            E_temp2 += square[j][i]
        E_i.append(E_temp1)
        E_j.append(E_temp2)

    
    chi2 = 0
    for i in range (0, len(square)):
        for j in range (0, len(square[i])):
            E_ij = (E_i[i] * E_j[j]) / N
            chi2 += (square[i][j] - E_ij) ** 2 / E_ij
    
    #chi2 = (N * (w1w2*nw1nw2 - w1nw2*w2nw1)**2) / ((w1w2+w1nw2)*(w1w2+w2nw1)*(nw1nw2+w1nw2)*(nw1nw2+w2nw1))

    print ("\n")
    print ("C(w1):\t\t", c_w1)
    print ("C(w2):\t\t", c_w2)
    print ("C(w1 && w2):\t", w1w2)
    print ("C(w1 && !w2):\t", w1nw2)
    print ("C(!w1 && w2):\t", w2nw1)
    print ("C(!w1 && !w2):\t", nw1nw2)
    print ("Total Words:\t", N, '\n')
    print ("0.05% Baseline:\t 3.841")
    print ("X^2:\t\t", chi2, '\n')

    if chi2 < 3.841:
        print("Null hypothesis accepted. \'"+w1+" "+w2+"\' is not a collocation.")
    else:
        print("Null hypothesis rejected. \'"+w1+" "+w2+"\' is a collocation.")
