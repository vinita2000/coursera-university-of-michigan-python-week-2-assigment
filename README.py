# coursera-university-of-michigan-python-week-2-assigment
python basics course // DICTIONARY ACCUMULATION ASSIGNMENT

#PROBLEM1
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits=0
for key in Junior:
    credits=credits+Junior[key]


PROBLEM2
str1 = "peter piper picked a peck of pickled peppers"
freq={}
for i in str1:
    if i not in freq:
        freq[i]=0
    freq[i]=freq[i]+1
    
PROBLEM3
s1 = "hello"
counts={}
for i in s1:
    if i not in counts:
        counts[i]=0
    counts[i]=counts[i]+1

PROBLEM4
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words={}
x=str1.split(" ")
for key in x:
    if key not in freq_words:
        freq_words[key]=0
    freq_words[key]=freq_words[key]+1


PROBLEM5
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d={}
x=sent.split(" ")
for key in x:
    if key not in wrd_d:
        wrd_d[key]=0
    wrd_d[key]=wrd_d[key]+1

PROBLEM6
sally = "sally sells sea shells by the sea shore"
characters={}

for key in sally:
    if key not in characters:
        characters[key]=0
    characters[key]=characters[key]+1
keys=list(characters.keys())
best_char=keys[0]
for key in keys:
    if characters[key]>characters[best_char]:
        best_char=key
        
        
PROBLEM7
sally = "sally sells sea shells by the sea shore and by the road"
characters={}

for key in sally:
    if key not in characters:
        characters[key]=0
    characters[key]=characters[key]+1
keys=list(characters.keys())
Worst_char=keys[0]
for key in keys:
    if characters[key]<characters[Worst_char]:
        Worst_char=key
        

PROBLEM8
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts={}
x=string1.lower()
for key in x:
    if key not in letter_counts:
        letter_counts[key]=0
    letter_counts[key]=letter_counts[key]+1
    #letter_counts[key]=letter_counts[key]+1    
    
PROBLEM9
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d={}
x=p.lower()
for key in x:
    if key not in low_d:
        low_d[key]=0
    low_d[key]=low_d[key]+1

