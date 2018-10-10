'''
Name		Jing Low
Section	27F3
Assignment	05
Due Date	February 16, 2018
'''
import nltk
import re

def pig_latin(word):
    #print(word)
    splitted = re.findall(r"^(.*?)([aeiou].*)", word)[0]
    #print(splitted)
    ans = (splitted[1]+splitted[0]+'ay')
    return ans

def problem_1a():
    text = input("Enter a word: ").lower()
    ans = pig_latin(text)
    print(ans)
    return ans

def problem_1b():
    text = input("Enter a string of text: ")
    words = [w.lower() for w in nltk.word_tokenize(text) if w.isalpha()]
    #print(words)
    result = ""
    for w in words:
        result += pig_latin(w) + ' '
    print (result)
    return result.strip()

def problem_2():
    text = input("Enter your Gainesville address: ").strip()
    #print(text)
    #using \s* below allows the program to accepts addresses with less or more spaces
    pattern = r'^[0-9]?[0-9]?[0-9]?[0-9]?[1-9]\s*(N|NW|NE|SW|S|SE|W|E)\s*[0-9]?[0-9]?[1-9]\s*(ST|ND|RD|TH)\s*(RD|AVE|DR|TERR|ST|CIR)\s*,\s*Gainesville,\s*FL\s*326[0-1][0-9]$'
    result = re.findall(pattern, text, re.IGNORECASE)
    #print(result)
    if len(result) > 0: 
        print ("This is a valid Gainesville address.")
    else:
        print("This is not a valid Gainesville address.")


