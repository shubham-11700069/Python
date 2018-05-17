def main():
    a=[10,20,5,49,32,68]
    print(mergeSort(a))
def mergeSort(a):
    key=len(a)//2
    left=a[0]
    right=a[-1]
    l=mergeSort(a[left:key])
    r=mergesort(a[key+1:right])
    return(merge(a,l,r))

def merge(a,l,r):
    if a[l]<a[r]:
        pass
    elif a[l]>a[r]:
        a[l],a[r]=a[r],a[l]
    return a
main()
