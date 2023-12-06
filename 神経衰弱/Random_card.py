import random
import os

tramps = []

for i in range(52):
    while True:
        pull=random.randint(0,51)
        if not(pull in tramps):
            tramps.append(pull)
            os.system('cls');
            print(tramps)
            break
        
print(tramps)

for i in range(51):
    for j in range(0,51-i,1):
        if tramps[j] > tramps[j+1]:
            put         = tramps[j+1]
            tramps[j+1] = tramps[j]
            tramps[j]   = put
            os.system('cls');print(tramps)
input()
