def main():
    n=int(input("enter the index: "))

    print("factorial of ",n,": ",fact(n))


def fact(n):
    if n==0:
        return 1
    
    else:
        return(fact(n-1)*n)


main()
