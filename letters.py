
import random

random.seed()

consos = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
freqc  = [ 2 , 3 , 6 , 2 , 3 , 2 , 1 , 1 , 5 , 4 , 8 , 4 , 1 , 9 , 9 , 9 , 1 , 1 , 1 , 1 , 1 ]
vowels = ['a','e','i','o','u']
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
