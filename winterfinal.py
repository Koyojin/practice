class Myselfclass:
    def __init__(self):
        self.myid=2021103992
        self.mybd=20011222
        self.mybdmonth="DEC"

    def getstudentid(self): 
        return str(self.myid)
    
    def getbithday(self):
        return str(self.mybd)

    def getstudentidbyinteger(self):
        return self.myid

    def getbirthdaybyintegersum(self):
        s=0
        for i in "20011222":
            s=s+int(i)

        return s

    def getmaxinteger(self):
        mixstr=str(self.mybd)+str(self.myid)
        maxv= 0
        for i in mixstr:
            inti=int(i)
            if inti > int(maxv):
                maxv= i
            else:
                pass
        return maxv

    def getaverageinteger(self):
        mixstr=str(self.mybd)+str(self.myid)
        s=0
        for i in mixstr:
            s=s+int(i)
        print (s)
        resavg= s/(len(mixstr))
        return resavg

    def getbirthdaybymonth(self):
        return self.mybdmonth

class Myrecodclass:

    def __init__(self):
            self.stuid=None
            self.deadline=None
            self.clasnum=None
            self.pri=None
           
    def makerecord(self,stuid,deadline,clasnum,pri):
        if type(stuid)!=str or type(deadline)!=str or type(clasnum)!=str or type(pri)!=int:
            return -1
        elif len(stuid)!=10 or len(deadline)!=8 or len(clasnum)!=4 or (pri!=3 and 2 and 1):
            return -2
        else:
            self.stuid=stuid
            self.deadline=deadline
            self.clasnum=clasnum
            self.pri=pri
            totallst=[self.stuid,self.deadline,self.clasnum,self.pri]
            return totallst

    def checkdelay(self,checknum,nowdate):
        if checknum==self.clasnum:
            if int(nowdate)<=int(self.deadline):
                return False
            elif int(nowdate)>int(self.deadline):
                return True
        else:
            return -1

 




b=Myrecodclass()
print(b. makerecord ("2021103992","20200101","A321",4))
print(b.stuid)
print(b. checkdelay("A321","20201222"))
