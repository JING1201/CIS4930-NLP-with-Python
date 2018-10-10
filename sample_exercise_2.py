import nltk
import random
from nltk.corpus import brown


def generate_model(cfdist, word, num) :
    result = []
    for i in range(num) :
        # Make sure it's not punctuation
        if word[0] < 'A' or word[0] > 'z' :
            i = i - 1
        else :
            result.append(word)
        possible = cfdist[word].keys()
        possible = list( possible )
        if len(possible) == 0 :
            return result
        # Find a random word from the most probable words
        topOfRange = int(len(possible)*.2)
        word = possible[random.randint(0,topOfRange)]
            
    return result

def generatePoem() :
    # Find bigrams and CFDs
    text = nltk.corpus.brown.words(categories='news')
    vocab = set(text)
    bgrams = nltk.bigrams(text)
    bgrams = list( bgrams )
    invertedBigrams = []
    for pair in bgrams :
        invertedBigrams.append([pair[1], pair[0]])
    invertedCfd = nltk.ConditionalFreqDist(invertedBigrams)
    
    # Get keys from pronouncing dictionary
    origDict = nltk.corpus.cmudict.dict()
    keys = origDict.keys()
    
    # Get corpus vocab
    inter = vocab.intersection(keys)
    
    # Create forward and backward dictionaries
    forwardDict = dict()
    reverseDict = dict()
    for each in inter :
        pron = origDict[each]
        temp = ''.join(pron[0][1:])
        forwardDict[each] = temp
        if temp in reverseDict :
            reverseDict[temp].append(each)
        else :
            reverseDict[temp] = [each]
    
    # Remove all rhyming sets with 3 or fewer words.
    for each in reverseDict.values() :
        if len(each) < 4 :
           for every in each :
                inter.remove(every)
    
    # Get a set of two (non-rhyming) rhyming words
    while 1 :
        [rhymeA, rhymeB] = random.sample(inter, 2)
        if forwardDict[rhymeA] != forwardDict[rhymeB] :
            break
    
    lines = []
    for i in range(0, 5):
        # This finds the third and fourth lines
        if i == 2 or i == 3 :
            numWords = 5
            result = 0
            # Make sure you get back the number of words you're looking for
            while result < numWords :
                listRhyming = reverseDict[forwardDict[rhymeB]]
                # If no more rhyming words, report a failure (try again)
                if len(listRhyming) == 0 :
                    return 0
                # Get next random rhyming word
                rhymeWord = random.sample(listRhyming, 1)[0]
                # Remove from list
                listRhyming.remove(rhymeWord)
                # Generate sentence backwards
                newLine = generate_model(invertedCfd, rhymeWord, numWords)
                newLine.reverse()
                result = len(newLine)
                # If sentence is correct length, put it together
                if result >= numWords :
                    newLine = ' '.join(newLine)
                    newLine = newLine.capitalize()
                    lines.append(newLine)
        # This finds the first, second and fifth lines
        else :
            numWords = 7
            result = 0
            while result < numWords :
                listRhyming = reverseDict[forwardDict[rhymeA]]
                if len(listRhyming) == 0 :
                    return 0
                rhymeWord = random.sample(listRhyming, 1)[0]
                listRhyming.remove(rhymeWord)
                newLine = generate_model(invertedCfd, rhymeWord, numWords)
                newLine.reverse()
                result = len(newLine)
                if result >= numWords :
                    newLine = ' '.join(newLine)
                    newLine = newLine.capitalize()
                    lines.append(newLine)
    
    # Assemble the lines into poems
    poem = ''
    i = 0
    for each in lines :
        if i == 4 :
            poem = poem + each + '.'
        else :
            poem = poem + each + ',\n'
        i = i + 1
    return poem

# It is possible that generation may fail if the right bigrams don't exist.  Keep trying until it works.
result = 0
while result == 0 :
    result = generatePoem()
    if result == 0 :
        print( "Poem generation failed because of bigram shortage.  Trying again." )


print( result )
