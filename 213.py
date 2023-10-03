#### ANSWER: START
def calculateSecond(d,h,m,s):
    ds= d*86400
    hs= h*3600
    ms= m*60
    ss= s
    ts= ds+hs+ms+ss
    return ts

def reverseString(w):
    wr= w[::-1]
    return wr

def calcTwoCharactersFromString(st1,f1,f2):
    f1n= st1.count(f1)
    f2n= st1.count(f2)
    ftn= f2n+f1n
    return ftn

def calcTwoCharactersFromStringV2(st1,f1,f2):
    if f1==f2:
        ftn= -1
    else:
        f1n= st1.count(f1)
        f2n= st1.count(f2)
        ftn= f2n+f1n
    return ftn

def calcTwoCharactersFromStringV3(st1,lst):
    ftn=0
    for i in lst:
        ftn= st1.count(i)+ftn
    return ftn

def mergeAndSortTwoList(lst1,lst2):
    tlst= lst1+lst2
    ftlst=[]
    for i in tlst:
        if i not in ftlst:
            ftlst.append(i)
    ftlst.sort()
    return ftlst

def mergeAndSortTwoListReverse(lst1,lst2):
    tlst= lst1+lst2
    ftlst=[]
    for i in tlst:
        if i not in ftlst:
            ftlst.append(i)
    ftlst.sort()
    ftlst.reverse()
    return ftlst

def searchMatchedCharacter(lst3,w1):
    relst=[]
    for i in lst3:
        if i[0]==w1:
            relst.append(i)
    relst.sort()
    return relst

def makeRandomTenIntegers():
    import random
    nlst= [1,2,3,4,5,6,7,8,9,10]
    random.shuffle(nlst)
    return nlst

def makeRandomIntegersExtended(f1,f2):
    if (f1<=0 or f2<=0) or (f1==f2) or (f1<f2):
        return -1
    else:
        import random
        nlst= list(range(f2,f1+1))
        random.shuffle(nlst)
        return nlst


#### ANSWER: END

#### Self Scoring : Start ####

TotalScore = 0

try:
    if calculateSecond(1,1,1,2) == 90062:
        TotalScore += 5
        print("[Q01-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q01-failed.1] Score - ", TotalScore)
    if calculateSecond(2,3,4,5) == 183845:
        TotalScore += 5
        print("[Q01-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q01-failed.2] Score - ", TotalScore)
except:
    print("[Q01-failed.except] Score - ", TotalScore)

try:
    if reverseString("Hello World!!") == '!!dlroW olleH':
        TotalScore += 5
        print("[Q02-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q02-failed.1] Score - ", TotalScore)
    if reverseString("Welcome to Hell!!") == '!!lleH ot emocleW':
        TotalScore += 5
        print("[Q02-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q02-failed.2] Score - ", TotalScore)
except:
    print("[Q02-failed.except] Score - ", TotalScore)

try:
    if calcTwoCharactersFromString("You only live once", 'o', 'o') == 6:
        TotalScore += 5
        print("[Q03-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q03-failed.1] Score - ", TotalScore)
    if calcTwoCharactersFromString("You only live once", 'o', 'Y') == 4:
        TotalScore += 5
        print("[Q03-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q03-failed.2] Score - ", TotalScore)
except:
    print("[Q03-failed.except] Score - ", TotalScore)

try: 
    if calcTwoCharactersFromStringV2("You only live once", 'o', 'o') == -1:
        TotalScore += 5
        print("[Q04-PASSED.1] Score - ", TotalScore)
    else:
        print("[Q04-failed.1] Score - ", TotalScore)
    if calcTwoCharactersFromStringV2("You only live once", 'o', 'Y') == 4:
        TotalScore += 5
        print("[Q04-PASSED.2] Score - ", TotalScore)
    else:
        print("[Q04-failed.2] Score - ", TotalScore)
except:
    print("[Q04-failed.except] Score - ", TotalScore)

try:
    if calcTwoCharactersFromStringV3("You only live once", ['a', 'o', 'o']) == 6:
        TotalScore += 10
        print("[Q05-PASSED] Score - ", TotalScore)
    else:
        print("[Q05-failed.try] Score - ", TotalScore)
except:
    print("[Q05-failed.except] Score - ", TotalScore)

try:
    if mergeAndSortTwoList([1,1,2,3,5,8,13,24,34,55], [1,1,2,3,4,5,6,7,8,9,10,11,12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 24, 34, 55]:
        TotalScore += 10
        print("[Q06-PASSED] Score - ", TotalScore)
    else:
        print("[Q06-failed.except] try - ", TotalScore)
except:
    print("[Q06-failed.except] Score - ", TotalScore)

try: 
    if mergeAndSortTwoListReverse([1,1,2,3,5,8,13,24,34,55], [1,1,2,3,4,5,6,7,8,9,10,11,12]) == [55, 34, 24, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
        TotalScore += 10
        print("[Q07-PASSED] Score - ", TotalScore)
    else:
        print("[Q07-failed.try] Score - ", TotalScore)
except:
    print("[Q07-failed.except] Score - ", TotalScore)

try:
    kingdoms = ['Bacteria', 'Protozoa','Chromista','Plantae','Fungi','Animalia']
    if searchMatchedCharacter(kingdoms, 'P') == ['Plantae', 'Protozoa']:
        TotalScore += 10
        print("[Q08-PASSED] Score - ", TotalScore)
    else:
        print("[Q08-failed.try] Score - ", TotalScore)
except:
    print("[Q08-failed.except] Score - ", TotalScore)

try:
    examResult = makeRandomTenIntegers()
    examResult.sort()
    if examResult == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        TotalScore += 10
        print("[Q09-PASSED] Score - ", TotalScore)
    else:
        print("[Q09-failed.try] Score - ", TotalScore)
except:
    print("[Q09-failed.except] Score - ", TotalScore)

try:
    examResult = makeRandomIntegersExtended(20,1)
    examResult.sort()
    if examResult == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        TotalScore += 10
        print("[Q10-PASSED] Score - ", TotalScore)
    else:
        print("[Q10-failed.try] Score - ", TotalScore)
except:
    print("[Q10-failed.except] Score - ", TotalScore)

#### Self Scoring : End ####

print("==>> FINAL SCORE: ", TotalScore)
