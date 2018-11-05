def main():
    n=int(input("enter the no. of items in list: "))
    lst=[]
    for i in range(n):
        lst.append(int(input()))

    print(selectionsort(lst,0,1))

def selectionsort(lst,low,high):
    for high in range (low,len(lst)):
        if lst[low]>lst[high]:
            lst[low],lst[high]=lst[high],lst[low]
    if low<len(lst):
        selectionsort(lst,low+1,high)

    return lst

main()
main()
                
        
    
