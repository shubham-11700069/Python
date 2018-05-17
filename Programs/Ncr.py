def ncr(n,r):
    c=[[0]*(r+1) for x in range (n+1)]
    for i in range (n+1):
        for j in range (r+1):
            if j==0:
                c[i][j]=1
            elif i==j:
                c[i][j]=1
            elif i>j:
                c[i][j]=c[i-1][j-1]+c[i-1][j]
    return c[n][r]
n=int(input("Enter value of n:"))
r=int(input("enter value of r:"))
print("ncr""=")
print(ncr(n,r))
