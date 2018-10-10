'''
Name		Jing Low
Section	    27F3
Assignment	11
Due Date	April 29, 2018
'''
import nltk

def noun_phrase():
    user_input = input('Do you want to input your own sentence (1) or try one of the examples (2)?\n')
    if user_input == '1':
        sentence = input('Input your own sentence here: ')
    elif user_input == '2':
        choice = input('''Please choose from the following examples: \n
                        (1) the receiving end\n
                        (2) assistant managing editor\n''')
        if choice == '1':
            sentence = 'the receiving end'
        elif choice == '2':
            sentence = 'assistant managing editor'
        else:
            print ('Invalid choice. Default sentence \'the receiving end\' is chosen. ')
            sentence = 'the receiving end'
    else:
        print ('Invalid choice. Default sentence \'the receiving end\' is chosen. ')
        sentence = 'the receiving end'
    
    grammar = r"""
            NP: {<DT|PP\$>?<JJ>*<NN>*<VBG>*<NN>}
                {<NNP>+}
            """
    cp = nltk.RegexpParser(grammar)

    tagged_words = nltk.pos_tag(nltk.word_tokenize(sentence))
    result = cp.parse(tagged_words)

    return result

def binary_parser(instruction):
    
    binary_grammar = nltk.CFG.fromstring("""
        INSTRUCTION -> 64BIT | 32BIT
        64BIT -> 32BIT 32BIT
        32BIT -> BYTE BYTE BYTE BYTE
        BYTE -> WORD WORD
        WORD -> BIT BIT BIT BIT
        BIT -> '0' | '1'
        """)
    
    parser = nltk.ChartParser(binary_grammar)
    for tree in parser.parse(instruction):
        print(tree)
    