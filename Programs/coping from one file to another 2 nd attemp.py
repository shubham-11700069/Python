f1=open("new.txt","r")

f2=open("nhn.txt","w")
for i in f1:
    s=f1.read()
    f2.write(s)
f1.close()
f2.close()
