def mergesort(a):
    l=0
    r=len(a)-1
    mid=(l+r)//2
    if len(a)>1:
        mergesort(a[l:mid])
        mergesort(a[mid+1:r])
        return(merge(a[l:mid],a[mid+1:r]))
def merge(q,b):
    i=len(q)
    j=len(b)
    m,n=0,0
    fl=[]
    k=0
    if m+n<i+j:
        if q[m]<b[n]:
            fl[k]=q[m]
            n+=1
            k+=1
        elif q[m]>b[n]:
            fl[k]=b[n]
            m+=1
            k+=1
        elif m==i and n!=j:
            fl[k]=b[n]
            k+=1
            n+=1
        elif n==j:
            fl[k]=q[m]
            k+=1
            m+=1
    print(f1)
    return fl
            


a=[10,20,5,9,12,50,70,60,80]
print(mergesort(a))
    
