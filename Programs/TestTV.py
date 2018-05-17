from TV import TV

def main():
    tv1=TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVol(4)

    tv2=TV()
    tv2.turnOn()
    tv2.channelUp()
    tv2.channelUp()
    tv2.volumeUp()

    print("tv1's channel is ",tv1.getchannel(),"and volume level" ,tv1.getVol())
    print("tv2's channel is ",tv2.getchannel(),"and volume level" ,tv2.getVol())
main()
