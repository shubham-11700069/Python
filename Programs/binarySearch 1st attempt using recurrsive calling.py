def binarysearch(lst,beg,end,item):
    mid=(beg+end)//2
    
    if item==lst[mid]:
        pos=mid
        return(mid+1)
    #reconfiguring the mid value
    elif item<lst[mid]: 
        end=mid-1
    else:
        beg=mid+1
    return(binarysearch(lst,beg,end,item))
    
    

def main():
    n=5
    lst=[10,20,30,40,50]

    lst=sorted(lst)
    print('entered' ,lst)
    item=int(input("enter the element you want to search: "))
    beg=0
    end=len(lst)-1
    mid=(beg+end)//2
    print("entered element is present at: ",(binarysearch(lst,beg,end,item)))

main()
        
