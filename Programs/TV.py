class TV:
    def __init__(self):
        self.channel=1
        self.volumelevel=1
        self.on=False

    def turnOn(self):
        self.on=True

    def turnOff(self):
        self.on=False

    def getchannel(self):
        return self.channel

    def setChannel(self, channel):
        if self.on and 1<=self.channel<=100:
            self.channel=channel

    def getVol(self):
        return self.volumelevel

    def setVol(self,volumelevel):
        if self.on and 1<=self.volumelevel<=10:
            self.volumelevel=volumelevel

    def channelUp(self):
        if self.on and self.channel<100:
            self.channel+=1

    def channelDown(self):
        if self.on and self.channel>1:
            self.channel-=1

    def volumeUp(self):
        if self.on and self.volumelevel<7:
            self.volumelevel+=1

    def volumeDown(self):
        if self.on and self.volumelevel>0:
            self.volumelevel-=1
            
    
