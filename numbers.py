

import sys
import random
import time
#import numpy as np

def riley(aNums, aTarg):
    ops = ['a','s','p','q']
    #lists
    lNumbers = []   #6! combinations
    lOperators = [] #4^5 combinations
    lInserts = []   #5! combinations
    dResults = {}   #6 results per solution, dictionary indexed on 3-tuple of indicies
    dPivot = {}     #dictionary indexed on result, containing Tracker strings
    #set up
    for i in range(100):
        lNumbers.append(random.sample(aNums,k=len(aNums)))
    for i in range(100):
        lOperators.append(random.choices(ops,k=5))
    for i in range(100):
        tempInsert = []
        tempInsert.append(random.choice([0,1,2,3,4]))
        tempInsert.append(random.choice([0,1,2,3]))
        tempInsert.append(random.choice([0,1,2]))
        tempInsert.append(random.choice([0,1]))
        tempInsert.append(0)
        lInserts.append(tempInsert)
    #print(lNumbers)
    #print(lOperators)
    #print(lInserts)
    for i,a in enumerate(lNumbers):
        for j,b in enumerate(lOperators):
            for k,c in enumerate(lInserts):
                lWorking = [x for x in a]
                #print("a: ", a)
                #print("b: ", b)
                #print("c: ", c)
                #print("lWorking",lWorking)
                #print(type(lWorking[0]))
                lTracker = [str(x) for x in a]
                #print("lTracker",lTracker)
                lIntermediateResults = []
                for l in range(5):
                    n1 = lWorking.pop(0)
                    n2 = lWorking.pop(0)
                    s1 = lTracker.pop(0)
                    s2 = lTracker.pop(0)
                    temp = None
                    sTemp = 'DEADBEEF'
                    if b[l] == 'a':
                        temp = n1+n2
                        sTemp = '('+s1+'+'+s2+')'
                    elif b[l] == 's':
                        temp = n1-n2
                        sTemp = '('+s1+'-'+s2+')'
                    elif b[l] == 'p':
                        temp = n1*n2
                        sTemp = '('+s1+'*'+s2+')'
                    elif b[l] == 'q':
                        if n2!=0 and n1%n2 == 0:
                            temp = n1//n2
                            sTemp = '('+s1+'/'+s2+')'
                        else:
                            lIntermediateResults.append(temp)
                            dResults[(i,j,k)] = lIntermediateResults
                            break
                    lWorking.insert(c[l],temp)
                    lTracker.insert(c[l],sTemp)
                    #print('lWorking: ', lWorking)
                    #print('lTracker: ', lTracker)
                    if temp == aTarg:
                        #print("SOLUTION! ",temp,"=",sTemp)
                        return str(temp)+'='+sTemp
                    lIntermediateResults.append(temp)
                dResults[(i,j,k)] = lIntermediateResults
    #No results found
    return "This one's impossible, actually!"

random.seed(344)

bigOnes = [100,75,50,25]
smallOnes = [10,9,8,7,6,5,4,3,2,1]

if sys.argv[1] not in ['0','1','2','3','4']:
    print("Must specify number of large ones, 0-4")
else:
    bigs = int(sys.argv[1])
    littles = 6-bigs
    nums = []
    nums += random.sample(bigOnes,k=bigs)
    nums += random.sample(smallOnes+smallOnes+smallOnes,k=littles)
    target = random.randint(100,999)
    for i in range(6):
        if i==0:
            print("\n"+"_ "*6+'\n\n')
        else:
            print("\n"+"_ "*(6-i)+' '.join([str(a) for a in nums][-i:])+'\n\n')
        time.sleep(1)
        print("\33[5A")
    for j in range(1000):
        rand = random.randint(100,999)
        print('     '+str(rand)+'\n'+' '.join([str(a) for a in nums]))
        print("...and the target...\n")
        time.sleep(0.002)
        print("\33[5A")
    print("    ",target)
    print(' '.join([str(a) for a in nums]))
    print("Your time starts...\n")
    time.sleep(5)
    print("\33[3A")
    print("Your time starts... now!")
    for i in range(30):
        print('     ',30-i, ' ')
        time.sleep(1)
        print("\33[2A")
    rachel = riley(nums,target)
    _ = input("Rachel, can it be done?")
    print(rachel)
