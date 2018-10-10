import nltk
from collections import defaultdict
from nltk.corpus import brown

def chunker( ) :
    untagged = brown.words()
    untagged = untagged[ 50000 : 50100 ]
    
    tokenizer = nltk.data.load( 'tokenizers/punkt/english.pickle' )
    untagged_sents = tokenizer.sentences_from_tokens( untagged )
    
    untagged_sents = list( untagged_sents )
    
    tagged_sents = brown.tagged_sents()[ 0 : 1000 ]
    t0 = nltk.DefaultTagger( 'NN' )
    t1 = nltk.UnigramTagger( tagged_sents, backoff=t0 )
    t2 = nltk.BigramTagger( tagged_sents, backoff=t1 )
    tagged_sents = []
    grammar = r"""
        NP: {<DT|JJ|NP.*|NN.*>+}
        PP: {<IN><NP>}
        VP: {<VB.*><NP|PP|CLAUSE>+$}
        """
    rp = nltk.RegexpParser(grammar)
    
    count = 1
    
    for each in untagged_sents :
        tagged = t2.tag( each )
        result = rp.parse( tagged )
        
        answer = input( 'Would you like to see the chunk tree for sentence #' + str( count ) + '? [y/n]:  ' )
        if ( answer == 'y' or answer == 'Y' ) :
            print( result )
            result.draw()
        count += 1

def cfg_generator( text ) :
    words = nltk.word_tokenize( text )
    
    tagged_sents = brown.tagged_sents( tagset="universal" )
    tagged_sents = tagged_sents[ 0 : 10000 ]
    t0 = nltk.DefaultTagger( 'NN' )
    t1 = nltk.UnigramTagger( tagged_sents, backoff=t0 )
    t2 = nltk.BigramTagger( tagged_sents, backoff=t1 )
    
    tagged = t2.tag( words )
    
    grammar = r"""
      NPHRASE: {<DET|ADJ|PRO|N.*>+}
      PPHRASE: {<P><NPHRASE>}
      VPHRASE: {<V><NPHRASE|PPHRASE|CLAUSE>+$}
      CLAUSE: {<NPHRASE><VPHRASE>}
      """
    
    rp = nltk.RegexpParser( grammar )
    chunked = rp.parse( tagged )
    
    tags = defaultdict(list)
    tagset = [ 'VERB', 'NOUN', 'PRO', 'ADP', 'DET' ,'CNJ', 'ADJ', 'ADV' ]
    for each in tagged :
        if each[1] not in tagset and [ each[0] ] not in tags[ 'UNK' ] :
            tags[ 'UNK' ].append( [ each[0] ] )
        elif ( [ each[0] ] not in tags[ each[1] ] ) :
            tags[ each[1] ].append( [ each[0] ] )
    
    tags['S'].append( get_production( chunked, tags, tagset ) )

    grammar = ""
    keys = [ 'S', 'NPHRASE', 'PPHRASE', 'VPHRASE', 'CLAUSE', 'VERB', 'NOUN', 'PRO', 'ADP', 'DET' ,'CNJ', 'ADJ', 'ADV', 'UNK' ]
    
    for each in keys :
        next = tags[ each ]
        if ( len( next ) == 0 ) :
            continue
        list_str = ''
        length = len( next )
        count = 0
        for production in next :
            for item in production :
                list_str += item + " "
            if count < length - 1 :
                list_str = list_str + '| '
            count = count + 1
        
        grammar = grammar + each + ' -> ' + list_str + '\n'
    
    answer = input( 'Would you like to see the grammar? [y/n]:  ' )
    if ( answer == 'y' or answer == 'Y' ) :
        print( grammar )
    
    return grammar		    
    
def get_production( chunked, tags, tagset ) :
    next = []
    for each in chunked :
        if ( isinstance( each, nltk.Tree ) ) :
            production = get_production( each, tags, tagset )
#			if ( production not in tags[ each.node ] ) :
            if ( production not in tags[ each.label() ] ) :
                tags[ each.label() ].append(production)
            next.append( each.label() )
        else :
            if ( each[1] in tagset ) :
                next.append( each[1] )
            else :
                next.append( 'UNK' )
    return next

print( 'Chunking selected sentences from Brown\n' )
chunker()

sentence = input('\n\nPlease enter a sentence (sans punctuation) for which you want to generate a context-free grammar... \n\n' )

# one sample sentence is...
# 'we went to the animal fair looking to see the birds and the bees there'

cfg_generator( sentence )

