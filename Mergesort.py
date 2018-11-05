'''
Created on 30-Oct-2017

@author: Gokulraj
'''

def mergesort(a,left,right):
    if len(right)-len(left)<=1:
        return(left)
    elif right-left>1:
        mid=(right+left)//2;
        l=a[left:mid]
        r=a[mid+1:right]
        mergesort(a,l,r)
        mergesort(a,l,r)
        merge(a,l,r)
def merge(A,B):
    (c,m,n)=([],len(A),len(B))
    i,j=0,0
   
    if i==m:
        c.append(B[j])
        j=j+1
    elif A[i]<=B[j]:
        c.append(A[i])
        i=i+1
    elif A[i]>B[j]:
        c.append(B[j])
        j=j+1
    else:
        c.append(A[i])
        i=i+1
    return(c)
            
a=[10,20,3,19,8,15,2,1]
left=0
right=len(a)-1
d=mergesort(a,left,right)
print(d)
