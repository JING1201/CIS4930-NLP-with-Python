'''
Name		Jing Low
Section	    27F3
Assignment	Extra Credit 02
Due Date	April 5, 2018
'''

import nltk
import os
import random
import re

def iRobot():
    corpus_root = r'D:\Academics\UF\CIS 4930\Loebner-logs-2003'
    folders = os.listdir(corpus_root)
    text = []
    for folder in folders:
        files = os.listdir(corpus_root+'\\'+folder)
        for file in files:
            f = open(corpus_root+'\\'+folder+'\\'+file, "r")
            for line in f.readlines():
                text.append(line)
            f.close()

    pattern = re.compile(r".*: (.*)") # for extracting the dialog
    pattern2 = re.compile(r"(.*):.*") # for extracting the line info
    labeled_sents = []
    questions = []
    words = set()
    for line in text:
        #print(line)
        processed_line = re.findall(pattern,line)
        if len(processed_line) > 0:
            line_info = re.findall(pattern2, line)
            if re.search('judge', line_info[0], re.IGNORECASE) or re.search('confederate', line_info[0], re.IGNORECASE):
                label = 'HUMAN'
            else:
                label = 'ROBOT'
            sents = nltk.sent_tokenize(processed_line[0])
            for sent in list(sents):
                if '?' in sent and label == 'HUMAN':
                    questions.append(sent)
                for w in nltk.word_tokenize(sent):
                    if w.isalpha():
                        words.add(w.lower())
            labeled_sents.append((processed_line[0], label))
    
    pronouns = ['i','you','u','they','us','we','them','he','she','him','her','me']
    modals = ['can', 'could', 'may', 'might', 'will', 'would', 'shall', 'should', 'must']
    
    def features(sent):
        features = {}
        tokenized_sent = [w.lower() for w in nltk.word_tokenize(sent)]
        
        for word in list(words):
            features['words({})'.format(word)] = (word in tokenized_sent)
        
        for pronoun in pronouns:
            features['pronouns'] = (pronoun in tokenized_sent)
            if features['pronouns']:
                break
        for modal in modals:
            features['modals'] = (modal in tokenized_sent)
            if features['modals']:
                break
        
        return features
    
    random.shuffle(labeled_sents)
    featuresets = [(features(d), c) for (d,c) in labeled_sents]

    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    question = random.choice(questions)
    print (question)
    user_ans = input('Your Answer:\t')
    print ('You are a:\t', classifier.classify(features(user_ans)))

    print ('Accuracy of the Classifier:\t', nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(5)

