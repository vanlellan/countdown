
import sys
import random
import time
#import numpy as np

def riley(aNums, aTarg):
    ops = ['a','s','p','q']
    #lists
    lNumbers = []   #6! combinations (720)
    lOperators = [] #4^5 combinations (1024)
    lInserts = []   #5! combinations (120)
    #dResults = {}   #6 results per solution, dictionary indexed on 3-tuple of indicies
    #dPivot = {}     #dictionary indexed on result, containing Tracker strings
    #set up
    for i in range(6):   #full: generate exhaustive list of all 6! combinations
        for ii in range(5):
            for iii in range(4):
                for iiii in range(3):
                    for iiiii in range(2):
                        copyNums = [a for a in aNums]
                        tempN = []
                        tempN.append(copyNums.pop(i))
                        tempN.append(copyNums.pop(ii))
                        tempN.append(copyNums.pop(iii))
                        tempN.append(copyNums.pop(iiii))
                        tempN.append(copyNums.pop(iiiii))
                        tempN.append(copyNums[0])
                        lNumbers.append(tempN)
    for i in range(4):  #full: generate exhaustive list of all 4^5 combinations
        for ii in range(4):
            for iii in range(4):
                for iiii in range(4):
                    for iiiii in range(4):
                        tempO = []
                        tempO.append(ops[i])
                        tempO.append(ops[ii])
                        tempO.append(ops[iii])
                        tempO.append(ops[iiii])
                        tempO.append(ops[iiiii])
                        lOperators.append(tempO)
    for i in range(5):   #full: generate exhaustive list of all 5! combinations
        for ii in range(4):
            for iii in range(3):
                for iiii in range(2):
                    tempI = [i,ii,iii,iiii,0]
                    lInserts.append(tempI)
#    for i in range(72*2):   #partial 
#        lNumbers.append(random.sample(aNums,k=len(aNums)))
#    for i in range(102):  #partial
#        lOperators.append(random.choices(ops,k=5))
#    for i in range(12):   #partial
#        tempInsert = []
#        tempInsert.append(random.choice([0,1,2,3,4]))
#        tempInsert.append(random.choice([0,1,2,3]))
#        tempInsert.append(random.choice([0,1,2]))
#        tempInsert.append(random.choice([0,1]))
#        tempInsert.append(0)
#        lInserts.append(tempInsert)
    for i,a in enumerate(lNumbers):
        for j,b in enumerate(lOperators):
            for k,c in enumerate(lInserts):
                lWorking = [x for x in a]
                lTracker = [str(x) for x in a]
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
                            #dResults[(i,j,k)] = lIntermediateResults
                            break
                    lWorking.insert(c[l],temp)
                    lTracker.insert(c[l],sTemp)
                    #print('lWorking: ', lWorking)
                    #print('lTracker: ', lTracker)
                    if temp == aTarg:
                        #print("SOLUTION! ",temp,"=",sTemp)
                        return str(temp)+'='+sTemp
                    lIntermediateResults.append(temp)
                #dResults[(i,j,k)] = lIntermediateResults
    #No results found
    return "This one's impossible, actually!"

random.seed()

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
    time.sleep(3)
    print("\33[3A")
    print("Your time starts... now!")
    for i in range(30):
        print('     ',30-i, ' ')
        time.sleep(1)
        print("\33[2A")
    rachel = riley(nums,target)
    _ = input("Rachel, can it be done?")
    print(rachel)
