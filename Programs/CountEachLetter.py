import os.path
def main():
    filename=input("enter a filename: ").strip()
    try:
        infile=open(filename,"r")
        counts=26*[0]
        for line in infile:
            countLetters(line.lower(), counts)

        for i in range(len(counts)):
            if counts[i]!=0:
                print(chr(ord("a")+i)+" appears "+str(counts[i])+(" time " if counts[i]==1 else " times ") )
                infile.close()
    except IOError:
        
            print("file does not exists")
def countLetters(line,counts):
    for ch in line:
        if ch.isalpha():
            counts[ord(ch)-ord("a")]+=1
main()
