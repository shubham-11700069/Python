import os.path
import sys

def main():
    r1=input("enter a source file: ").strip()
    r2=input("enter a destination file: ").strip()
    try:
        if os.path.isfile(r2):
            print(r2 +" file already exists")
            sys.exit()

        infile=open(r1,"r")
        outfile=open(r2,"w")
        countLines=countChar=0
        for line in infile:
            countLines+=1
            countChar+=len(line)
            outfile.write(line)
        print(countLines,"lines & ",countChar,"characters are copied")
        infile.close()
        outfile.close()
    except:
        if os.path.isfile(r1)==False:
            print("file does not exist" )

main()
        
