def mergesort(a,left,right):
    l,r=0,0;
    if (right-left<=1):
        return (a[left]);
    elif (right-left>1):
        mid=(right+left)//2
        l=mergesort(a,l,mid)
        r=mergesort(a,mid,r)
        return (merge(l,r));
        
def merge(a,b):
    c=[]
    m=(a)
    n=(b)
    i,j=0,0
    while i+j<=m+n:
        if i==m and j<n:
            c.append(b[j])
            j=j+1;
        elif(a[i]<b[j]):
            c.append(a[i]);
            i=i+1;
        elif (a[i]>b[j]):
            c.append(b[j])
            j=j+1;
        else:
            c.append(a[i])
            i=i+1;
        if i==m or j==n:
            break;
    print(c)
    return c;
    
l1=[100,30,20,15,304,87];
left=0;

right=len(l1)-1;
d=mergesort(l1,left,right);

