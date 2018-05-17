def ispalindrome(p):
    if len(p)<=1:
        return True

    elif p[0]!=p[len(p)-1]:
        return False
    else:
        ispalindrome(p[1:len(p)-1])

def main():
    s=input("enter string: ")
    if ispalindrome(s)==False:
        ans=False
    else:
        ans=True
    print(ans)

main()
main()
main()
main()
