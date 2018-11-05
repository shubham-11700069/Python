def main():
    hex=input("Enter hexadecimal number: ")

    decimal=hextodecimal(hex.upper())
    if decimal==None:
        print("Incorrect hex number")

    else:
        print("the decimal value for hex number",hex,"is",decimal)



def hextodecimal(hex):
    decimalvalue=0
    for i in range(len(hex)):
        ch=hex[i]
        if 'A'<=ch<='F' or '0'<=ch<='9':
            decimalvalue=decimalvalue*16+\
                          hexchartodecimal(ch)

        else:
            return None

    return decimalvalue

def hexchartodecimal(ch):
    if 'A'<=ch<='F':
        return 10+ord(ch)-ord('A')
    else:
        return ord(ch)-ord('0')

main()
