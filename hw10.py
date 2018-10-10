'''
Name		Jing Low
Section	    27F3
Assignment	10
Due Date	April 13, 2018
'''

import nltk
import inflect
from nltk.corpus import brown
from nltk.corpus import movie_reviews
import random
from nltk.corpus import wordnet as wn

def problem_5_15a():

    # getting only singular and plural common and proper nouns
    all_tagged_nouns = [(w.lower(), tag) for (w, tag) in brown.tagged_words() if 
             (tag.startswith('NN') or tag.startswith('NNS') or tag.startswith('NP') or tag.startswith('NPS')) 
            and not (tag.startswith('NN$') or tag.startswith('NP$') or tag.startswith('NPS$') or tag.startswith('NNS$'))]
    all_nouns = [w for (w, tag) in all_tagged_nouns]
    noun_set = set(all_nouns)

    fq_nouns = nltk.FreqDist(all_nouns)
    inf = inflect.engine() 

    ans = set()
    for w in list(noun_set):
        if inf.singular_noun(w) is False: #if noun is singular (because it cannot be converted to plural)
            plural_w = inf.plural_noun(w)
            if fq_nouns[plural_w] > fq_nouns[w]:
                ans.add ((w, plural_w))
        else:
            singular_w = inf.singular_noun(w)
            if fq_nouns[singular_w] < fq_nouns[w]:
                ans.add ((singular_w, w))
    
    print ('These nouns appear in their plural forms more often than in their singular forms:')
    for i in list(ans):
        print (i)

def problem_5_15b():
    
    tagged = [(w.lower(), tag) for (w, tag) in brown.tagged_words() if w.isalpha()]
    tagged_words = {}
    for (w, tag) in tagged:
        if w not in tagged_words.keys():
            tagged_words[w] = [tag]
        else:
            if tag not in tagged_words[w]:
                tagged_words[w].append(tag)
    
    max_word = []
    max_tags = 0
    for w in tagged_words.keys():
        if len(tagged_words[w]) > max_tags:
            max_tags = len(tagged_words[w])
            max_word = [w]
        elif len(tagged_words[w]) == max_tags:
            max_word.append(w)
    
    print ('The word \'', max_word[0], '\' has the most number of distinct tags.')
    print ('The tags are: ')
    for tag in tagged_words[max_word[0]]:
        print (tag)
        nltk.help.upenn_tagset(tag)

def problem_5_15c():
    
    tags = [tag for (w, tag) in brown.tagged_words()]
    fq_tags = nltk.FreqDist(tags)
    ans = fq_tags.most_common(20)
    
    print ('The 20 most common tags are: ')
    for (tag, count) in ans:
        print (tag)
        nltk.help.upenn_tagset(tag)

def problem_5_15d():
    
    tags = [tag for (w, tag) in brown.tagged_words()]
    backward_tags = list(reversed(tags))
    backward_tags_2 = backward_tags
    bigrams = []
    for i in range (0, len(backward_tags)):
        if (backward_tags[i].startswith('NN') or backward_tags[i].startswith('NNS') or backward_tags[i].startswith('NP') or backward_tags[i].startswith('NPS')):
            backward_tags[i] = 'NOUN'
        if i > 0:
            bigrams.append((backward_tags[i-1], backward_tags_2[i]))
    
    backward_fq = nltk.ConditionalFreqDist(bigrams)

    ans = backward_fq['NOUN'].most_common(20)

    print ('Nouns are most commonly preceded by the tags below: ')
    for (tag, count) in ans:
        print (tag)
        nltk.help.upenn_tagset(tag)

def problem_6_8():
    documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    all_synsets = nltk.FreqDist(wn.synsets(w)[0] for w in movie_reviews.words() if len(wn.synsets(w))>0)
    synset_features = list(all_synsets)[:2000]
    
    def document_features(document): 
        document_synsets = set([wn.synsets(w)[0] for w in document if len(wn.synsets(w))>0]) 
        features = {}
        for synset in synset_features:
            features['contains({})'.format(synset)] = (synset in document_synsets)
        return features
    
    random.shuffle(documents)

    featuresets = [(document_features(d), c) for (d,c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    print('The accuracy of the classifier is: ', nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(5)