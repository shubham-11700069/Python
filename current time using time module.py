
import time
time.time()
totalsecs=int(time.time())
currsec=totalsecs%60
totalminutes=totalsecs//60
currminutes=totalminutes//60
currminutes=totalminutes%60
totalhours=totalminutes//60
currenthours=totalhours%60
print(currenthours,"",currminutes,"",currsec)
currenthours +=5
currminutes +=30
print(currenthours,"",currminutes,"",currsec)
