fibdict={0:0,1:1}
def fibonacci(n):
    if n in fibdict:
        return fibdict[n]
    else:
        fibdict[n]=fibonacci(n-1)+fibonacci(n-2)
        return fibdict[n]

def main():
    n=int(input("enter index: "))

    print(fibonacci(n))

main()
main()
main()
