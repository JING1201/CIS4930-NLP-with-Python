'''
Name		Jing Low
Section	    27F3
Assignment	06
Due Date	February 21, 2018
'''
import re
import nltk
import os

def regExT9(c):
    t = c.lower()
    if t=='a' or t=='b' or t=='c':
        return "[2abc]"
    elif t=='d' or t=='e' or t=='f':
        return "[3def]"
    elif t=='g' or t=='h' or t=='i':
        return "[4ghi]"
    elif t=='j' or t=='k' or t=='l':
        return "[5jkl]"
    elif t=='m' or t=='n' or t=='o':
        return "[6mno]"
    elif t=='p' or t=='q' or t=='r' or t=='s':
        return "[7pqrs]"
    elif t=='t' or t=='u' or t=='v':
        return "[8tuv]"
    elif t=='w' or t=='x' or t=='y' or t=='z':
        return "[9wxyz]"

def getPattern(word):
    pattern = ""
    for c in word:
        pattern += regExT9(c)
    return pattern

def translate (user_input):
    #read in the sbcorpus
    corpus_root = r'D:\Academics\UF\CIS 4930\sbcorpus'
    files = os.listdir(corpus_root)
    text = []
    for file in files:
        f = open(corpus_root+'\\'+file, "r")
        text.append(f.readlines())
        f.close()

    pattern = re.compile(r"([a-z|A-Z]+(?:[-='][a-z|A-Z]+)?)")

    processed = []
    for t in text:
        for sent in t:
            all_words = re.findall(pattern, sent)
            #further processing to filter out unwanted words
            processed += [w.replace("=","") for w in all_words 
                            if w=='I' or 
                            (w[0].isalpha() and not (w.isupper() or w=='Hx' or len(w)==1))]
    
    corpus = nltk.Text(processed)
    bigrams = nltk.bigrams(corpus)
    cfd = nltk.ConditionalFreqDist(bigrams)

    message = nltk.word_tokenize(user_input)

    ans = [message[0]]
    for i in range(1,len(message)):
        if not message[i-1].isalpha():
            ans.append(message[i])
        elif message[i].isalpha():
            #find the next words that have the same stroke as the next given word
            keys =[w for w in list(cfd[ans[i-1]]) if re.search('^'+getPattern(message[i])+'$', w)]
            #find maximum freq among these keys
            max_freq = 0
            max_key = ""
            for key in keys:
                if cfd[ans[i-1]][key] > max_freq:
                    max_freq = cfd[ans[i-1]][key]
                    max_key = key
            if max_key=="":
                ans.append(message[i])
            else:
                ans.append(max_key)
            #print(key)
        else:
            ans.append(message[i])
    
    output = ans[0]
    for i in range (1, len(ans)):
        w = ans[i]
        if w=='.' or w==',' or w=='?' or w=='!':
            output += w
        else:
            output += " "+w
    
    print(output)

def main():
    user_input = input("Enter a mistyped string: ")
    if not user_input == "":
        translate(user_input)
    else:
        print("Please enter a string to begin with.")

if __name__ == "__main__":
    main()

