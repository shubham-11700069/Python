def merge(left,right,A):
    i=j=k=0
    while(i<len(left) and j<len(right)):
        if (left[i]<right[j]):
            A[k]=left[i]
            i+=1

        else:
            A[k]=right[j]
            j+=1

        k+=1

    while(i<len(left)):
        A[k]=left[i]
        i+=1
        k+=1

    while(j<len(right)):
        A[k]=right[j]
        j+=1
        k+=1


def mergeSort(A):
    left=[]
    right=[]
    n=len(A)
    if(n<2):
        return
    mid=n//2
    for i in range(mid):
        left.append(A[i])
    for i in range (mid,n):
        right.append(A[i])

    mergeSort(left)
    mergeSort(right)
    merge(left,right,A)

A=[2,4,1,3,8,9,0,-1,-2]
mergeSort(A)
print(A)
