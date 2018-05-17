def palindrome(s):
    for i in range(len(s)):
        
        if s[i]!=s[-i-1]:
            return False
        
def main():
    s=input("enter the string:")
    if(palindrome(s)==False):
        print("not palindrome")
    else:
        print ("is palindrome")

main()
main()
            
