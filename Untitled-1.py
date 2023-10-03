class RemoteControl:
    def __init__(self):
        self.enabledchannellist=[]
        self.nowchannel=[]
       
  
    def poweronremotecontrol(self,chanlist):
        self.enabledchannellist=chanlist
        self.nowchannel=self.enabledchannellist[0]

        chancount= len(self.enabledchannellist)
        return chancount

    def gotochannel(self,wantnum):
        for i in self.enabledchannellist:
            if i[0]==wantnum:
                self.nowchannel=i
                
            else:
                pass
        return self.nowchannel[1]
        
        
    def nextchannel(self):
        ncindex= self.enabledchannellist.index(self.nowchannel)+1
        if self.enabledchannellist.index(self.nowchannel)==len(self.enabledchannellist)-1:
            return self.nowchannel[1]
        else:
            return self.enabledchannellist[ncindex][1]

    def previouschannel(self):
        pcindex= self.enabledchannellist.index(self.nowchannel)-1
        if self.enabledchannellist.index(self.nowchannel)==0:
            return self.enabledchannellist[len(self.enabledchannellist)-1][1]
        else:
            return self.enabledchannellist[pcindex][1]

    def blockchannel(self):
        ncindex= self.enabledchannellist.index(self.nowchannel)+1
        if self.enabledchannellist.index(self.nowchannel)==len(self.enabledchannellist)-1:
            kk=self.nowchannel[1]
        else:
            kk=self.enabledchannellist[ncindex][1]

        del self.enabledchannellist[0]
        return kk
        


a=RemoteControl()
a.poweronremotecontrol([[0,"x"],[1,"y"],[2,"z"]])
print(a.enabledchannellist)
print(a.nowchannel)
print(a.gotochannel(1))
print(a.nextchannel())
print(a.gotochannel(0))
print(a.previouschannel())
