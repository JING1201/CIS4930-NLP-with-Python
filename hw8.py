'''
Name		Jing Low
Section	    27F3
Assignment	08
Due Date	March 23, 2018
'''

import nltk, re
from nltk.corpus import brown, treebank

class POS_Tag_Data :
 
 # given a corpus,
 # place the tuples of word/tag pairs into tagged
 # make the words in tagged / words lists lower case
 # use the punctuation selection provided
    def __init__( self, corpus, punctuation=False, universal=True ) :
        
        # when universal is True, use the universal tagset
        if universal:
            tagged_orig = corpus.tagged_words(tagset = "universal")
        else:
            tagged_orig = corpus.tagged_words()

        # when punctuation is False, take it out
        if punctuation == False:
            self.tagged = [(w.lower(), tag) for (w, tag) in tagged_orig if w.isalpha()]
        else:
            self.tagged = [(w.lower(), tag) for (w, tag) in tagged_orig]

        self.tags = [tag for (w, tag) in self.tagged]
        self.words = [w for (w, tag) in self.tagged]

    # find all index positions of the tag provided
    def all_tag_inds( self, tag ) :
        inds = [i for i in range (0, len(self.tags)) if self.tags[i] == tag]
        return inds
    
    # find all index positions of the word provided
    def all_word_inds( self, word ) :
        inds = [i for i in range (0, len(self.words)) if self.words[i] == word.lower()]
        return inds