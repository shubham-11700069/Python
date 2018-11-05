T=int(input())
def is_anagram(str1, str2):
    list_str1 = list(str1)
    
    list_str1.sort()
    list_str2 = list(str2)
    #list_str2.sort()
    return (list_str1 == list_str2)
for i in range(T):
    opt=0

    L=int(input())
    A=str(input())
    B=str(input())
    for j in range(len(A)):
        for k in range(len(A)):
            for l in range(k):
                if is_anagram(A[j:k],B[(abs(l))%3:(abs(l-k+1))%3]):
                    opt+=1
    
    print("Case #"+str(i+1)+": "+str(opt))
