Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:07:06) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.book import *
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
>>> grail_fd=FreqDist(text6)
>>> grail_fd.tabulate()
            :             .             !             ,             '             [             ]           the             I        ARTHUR             ?           you             a            of            --            to             s           and             #           ...            Oh            it            is             -            in          that             t     LAUNCELOT            No             1          your           not       GALAHAD        KNIGHT          What        FATHER            we      BEDEVERE           You            We          this            no          Well          HEAD         GUARD          have           Sir           are             A           And      VILLAGER            on            Ni            He            me          boom            he            be           Yes             2            ha            re           her         ROBIN          clop            my          away          with         witch       KNIGHTS        Arthur            up            It           him            do             m         Grail          here           out           for           but         BLACK           one           The           can          Burn            us       singing           TIM        mumble           all        FRENCH         music        squeak           got         Right          what          King            at           don          Come       Camelot         Hello            uh       HERBERT           Who     Launcelot          just         there           was         SCENE            if       SOLDIER          tell          Look          Holy          must          will            go         going          dead           his            am          That        DENNIS         right           Run           who            ve         shall          from            so           get            '.            ll         think         Robin          they          come       Knights        castle           off          very         CROWD          know        GUESTS           see         could      NARRATOR            Ha         clang          name            OF         brave           saw       CARTOON          Stop           sir            Uh          were  BRIDGEKEEPER          clap           Shh           But         DINGO          like          then          into            as         There            NI           sayTraceback (most recent call last):

  File "<pyshell#3>", line 1, in <module>
    grail_fd.tabulate()
  File "C:\Users\lowji\AppData\Local\Programs\Python\Python35-32\lib\site-packages\nltk\probability.py", line 323, in tabulate
    print("%*s" % (width, samples[i]), end=' ')
  File "C:\Users\lowji\AppData\Local\Programs\Python\Python35-32\lib\idlelib\PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> grail_fd.tabulate(10)
     :      .      !      ,      '      [      ]    the      I ARTHUR 
  1197    816    801    731    421    319    312    299    255    225 
>>> grail_fd.key("knight")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    grail_fd.key("knight")
AttributeError: 'FreqDist' object has no attribute 'key'
>>> grail_fd(knight)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    grail_fd(knight)
NameError: name 'knight' is not defined
>>> grail_fd('knight')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    grail_fd('knight')
TypeError: 'FreqDist' object is not callable
>>> grail_fd.freq('knight')
0.00029468969175458243
>>> text6.count("[")
319
>>> grail_grams=list(bigrams(text6))
>>> grail_grams[:30]
[('SCENE', '1'), ('1', ':'), (':', '['), ('[', 'wind'), ('wind', ']'), (']', '['), ('[', 'clop'), ('clop', 'clop'), ('clop', 'clop'), ('clop', ']'), (']', 'KING'), ('KING', 'ARTHUR'), ('ARTHUR', ':'), (':', 'Whoa'), ('Whoa', 'there'), ('there', '!'), ('!', '['), ('[', 'clop'), ('clop', 'clop'), ('clop', 'clop'), ('clop', ']'), (']', 'SOLDIER'), ('SOLDIER', '#'), ('#', '1'), ('1', ':'), (':', 'Halt'), ('Halt', '!'), ('!', 'Who'), ('Who', 'goes'), ('goes', 'there')]
>>> grail_grams[7]
('clop', 'clop')
>>> grail_grams_fd=FreqDist(grail_grams)
>>> grail_grams_fd[grail_grams[7])
SyntaxError: invalid syntax
>>> grail_grams_fd[grail_grams[7]]
26
>>> grail_grams_fd.tabulate(10)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    grail_grams_fd.tabulate(10)
  File "C:\Users\lowji\AppData\Local\Programs\Python\Python35-32\lib\site-packages\nltk\probability.py", line 319, in tabulate
    width = max(len("%s" % s) for s in samples)
  File "C:\Users\lowji\AppData\Local\Programs\Python\Python35-32\lib\site-packages\nltk\probability.py", line 319, in <genexpr>
    width = max(len("%s" % s) for s in samples)
TypeError: not all arguments converted during string formatting
>>> grail_grams_fd.tabulate(5)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    grail_grams_fd.tabulate(5)
  File "C:\Users\lowji\AppData\Local\Programs\Python\Python35-32\lib\site-packages\nltk\probability.py", line 319, in tabulate
    width = max(len("%s" % s) for s in samples)
  File "C:\Users\lowji\AppData\Local\Programs\Python\Python35-32\lib\site-packages\nltk\probability.py", line 319, in <genexpr>
    width = max(len("%s" % s) for s in samples)
TypeError: not all arguments converted during string formatting
>>> grail_grams_fd['clop']
0
>>> grail_fd['clop']
39
>>> text1.index('call')
16007
>>> text1.index('Call')
3820
>>> text1.index('Call me Ishmael')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    text1.index('Call me Ishmael')
  File "C:\Users\lowji\AppData\Local\Programs\Python\Python35-32\lib\site-packages\nltk\text.py", line 373, in index
    return self.tokens.index(word)
ValueError: 'Call me Ishmael' is not in list
>>> text1.index('Ishmael')
4714
>>> grail_set=set(text6)
>>> [word for word in grail_set if len(word)==2]
['15', 'va', "'.", 'we', "'?", 'la', 'Um', 'my', 'Do', '11', 'We', 'He', 'ho', 'Or', "'!", '..', 'ni', 'oh', 'Go', 'To', 'Ah', '23', '.)', 'on', 'no', 'At', 'Is', '13', 'Be', 'do', 'ye', 'em', 'of', 'Ha', '!]', 'is', 'be', 'Oh', 'er', 'as', 'eh', 'An', '20', 'de', '--', 'am', 'us', 'uh', '12', 'Of', 'By', 'OF', '22', 'So', 'It', 'up', 'by', 'oo', 'NI', 'In', '?!', 'Am', 'Ow', 're', 'so', 'um', 'bi', 'go', 'ju', "',", 'll', 'Ho', '14', 'un', ".'", 'If', 'or', 'in', 'Ay', 'My', 'As', 'me', 'Eh', 'On', 'to', '19', 'Uh', 'he', '10', '!,', 'Nu', '18', '17', '16', 'Hm', 'Ni', '!)', 've', '21', ",'", 'No', 'it', 'if', '24', 'ha', 'an', 'Un', 'at']
>>> numbers=[5,1,5,3,4,8,3,5,2,4]
>>> list=[]
>>> data=""
>>> for item in numbers:
	list.append(item)
	data=data+' '+str(item)

	
>>> print(list)
[5, 1, 5, 3, 4, 8, 3, 5, 2, 4]
>>> print(data)
 5 1 5 3 4 8 3 5 2 4
>>> 'im trying to try this'.split()
['im', 'trying', 'to', 'try', 'this']
>>> ' '.join(['test','the','usage','of','join'])
'test the usage of join'
>>> def postfix( word, postfixes):
	for suffix in postfixes:
		# if word[-len(suffix):] == suffix:
		if word.endswith( suffix ):
			return word[ : -len(suffix)]
		return word

	
>>> def prefix ( word, prefixes ):
	for affix in prefixes:
		# if word[:len(affix)] == affix:
		if word.startswith(affix):
			return word[len(affix):]
		return word

	
>>> root = 'immaturely'
>>> postfix(root,['ly','ing','s'])
'immature'
>>> prefix(root,['a','un','im','pre'])
'immaturely'
>>> def prefix ( word, prefixes ):
	for affix in prefixes:
		# if word[:len(affix)] == affix:
		if word.startswith(affix):
			return word[len(affix):]
	return word

>>> prefix(root,['a','un','im','pre'])
'maturely'
>>> def main():
	root = input ("Enter a string:")
	root = postfix(root, ['ing','ly','s'])
	root = prefix(root,['a','im','un','pre'])
	print(root)

	
>>> main()
Enter a string:Jing
J
>>> main()
Enter a string:unhappy
happy
>>> main()
Enter a string:string
str
>>> main()
Enter a string:unknowingly
knowingly
>>> def postfix( word, postfixes):
	for suffix in postfixes:
		# if word[-len(suffix):] == suffix:
		if word.endswith( suffix ):
			return word[ : -len(suffix)]
	return word

>>> main()
Enter a string:unknowingly
knowing
>>> 
