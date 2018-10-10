'''
Name		Jing Low
Section	    27F3
Assignment	09
Due Date	April 6, 2018
'''
import nltk
import pandas

def confusion_matrix (gold_standard, test_tagged, tag):

    table = [[0,0],[0,0]]
    for i in range (0, len(gold_standard)):
        test_tag = test_tagged[i][1]
        gold_tag = gold_standard[i][1]
        if test_tag == gold_tag:
            if test_tag == tag: 
                table[0][0]+=1 #TP
            else:
                table[1][1]+=1 #TN
        else:
            if test_tag == tag: 
                table[0][1]+=1 #FP
            elif gold_tag == tag:
                table[1][0]+=1 #FN
            else:
                table[1][1]+=1
    
    print(pandas.DataFrame(table, [['PREDICTION',''],['Positive','Negative']], [['TRUTH',''],['Positive','Negative']]))
    
    return table

def precision (gold_standard, test_tagged, tag):
    
    table = confusion_matrix (gold_standard, test_tagged, tag)

    #precision = TP/(TP+FP)
    precision = table[0][0]/(table[0][0]+table[0][1])
    return precision

def recall (gold_standard, test_tagged, tag):
    
    table = confusion_matrix (gold_standard, test_tagged, tag)
    
    # recall = TP/(TP+FN)
    recall = table[0][0]/(table[0][0]+table[1][0])
    return recall

def fMeasure (gold_standard, test_tagged, tag):
    
    table = confusion_matrix (gold_standard, test_tagged, tag)
    
    #precision = TP/(TP+FP)
    precision = table[0][0]/(table[0][0]+table[0][1])
    # recall = TP/(TP+FN)
    recall = table[0][0]/(table[0][0]+table[1][0])
    
    fmeasure = (2 * precision * recall)/(precision + recall)

    return fmeasure

