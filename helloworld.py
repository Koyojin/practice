#2
class Myselfclass:
    def getstudentid(self):
        return 1111111111
    
    def gerbirthday(self):
        return 20011222
    
    def gettermproject(self):
        return "aaaaaaaa"
#3
class integeraccumlator:
    L=[]
    
    def getnewinteger(self,a):
        s=0
        self.L.append(a)
        for i in self.L:
            s= s+i
        result= s/(len(self.L))
        return result

    def getaccumlatedintegers(self):
        return self.L

    def getaverage(self):
        s=0
        for i in self.L:
            s= s+i
        result= s/(len(self.L))
        return result
    

#4
def claintegerfromstring(numstr):
    nnumstr=str(numstr)
    s1=0
    for i in nnumstr:
        if  i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print (i)
        else:
            pass
    return s1



#6
class stringaccumlator:
    def putnewstring(s):
        return len(s)


k= integeraccumlator()
k.getnewinteger(5)
k.getnewinteger(6)
print(k.getnewinteger(9))

print(k.getaccumlatedintegers())
print(k.getaverage())
a= Myselfclass()
print(a.gerbirthday())

print(claintegerfromstring("1283kkk976"))

