
def rechelper(lst,key,low,high):
    if low>high:
        return False
    mid=(low+high)//2
    if(key <lst[mid]):
        return rechelper(lst,key,low,mid-1)
    elif key==lst[mid]:
        return mid+1
    else:
        return rechelper(lst,key,mid+1,high)

def main():
    lst=[3,5,6,8,9,12,34,36]
    low=0
    high=len(lst)-1
    key=344
    print(rechelper(lst,key,low,high))

   
main()
