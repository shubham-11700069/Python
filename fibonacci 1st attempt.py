fibdict={}
n=int(input("you want upto: "))
fibdict[0]=0
fibdict[1]=1
for j in range(2,n):
    fibdict[j]=(fibdict[j-1]+fibdict[j-2])

print(fibdict)
