



import sys
import random

random.seed()

bigOnes = ['100','75','50','25']
smallOnes = ['10','9','8','7','6','5','4','3','2','1']

if sys.argv[1] not in ['0','1','2','3','4']:
    print("Must specify number of large ones, 0-4")
else:
    bigs = int(sys.argv[1])
    littles = 6-bigs
    numbers = []
    numbers += random.sample(bigOnes,k=bigs)
    numbers += random.sample(smallOnes+smallOnes+smallOnes,k=littles)
    target = random.randint(100,999)
    print("    ",target)
    print(' '.join([str(a) for a in numbers]))

