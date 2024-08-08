
import random

random.seed()

consos = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
freqc  = [ 2 , 3 , 6 , 2 , 3 , 2 , 1 , 1 , 5 , 4 , 8 , 4 , 1 , 9 , 9 , 9 , 1 , 1 , 1 , 1 , 1 ]
vowels = ['A','E','I','O','U']
freqv  = [ 15, 21, 13, 13, 5 ]

vstack = []
for i,a in enumerate(freqv):
    vstack += list(vowels[i])*a
random.shuffle(vstack)

cstack = []
for i,a in enumerate(freqc):
    cstack += list(consos[i])*a
random.shuffle(cstack)

letters = []
while len(letters) < 9:
    request = input("Consonant (c), or Vowel (v)? ...")
    if request in ['c', 'C']:
        letters.append(cstack.pop())
    elif request in ['v', 'V']:
        letters.append(vstack.pop())
    else:
        print("ERROR: must choose c or v...")
    print( ' '.join(letters))
