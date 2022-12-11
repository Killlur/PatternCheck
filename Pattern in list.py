import random

def PatternInRange(number,o=10):
    for _ in range(number):
        genelist=[random.choice(('g','c','a','t')) for _ in range(o)]
        outputlist=[]

        for x in range(len(genelist)-3):
            if (str(genelist[x]),str(genelist[x+1]),str(genelist[x+2]),str(genelist[x+3])) == ('g','c','a','t'):
                outputlist.append((x,x+1,x+2,x+3))

        if outputlist:
            print(genelist)
            print(outputlist)


a = input('How many times do you want to run this -- ')
o = input('How many numbers in each list(optional) -- ')
PatternInRange(int(a), int(o))





