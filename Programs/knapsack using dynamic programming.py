def knapsack (n,maxW,W,P):
    bag=[[0]*(maxW +1) for i in range (n+1)]
    for i in range(n+1):
        for j in range(maxW+1):
            if i==0:
                bag[i][j]=0
            elif j==0:
                bag[i][j]=0
            else:
                if W[i]<=j:
                    if P[i]+bag[i-1][j-W[i]]>bag[i-1][j]:
                        bag[i][j]=P[i]+bag[i-1][j-W[i]]
                    else:
                        bag[i][j]=bag[i-1][j]
                else:
                    bag[i][j]=bag[i-1][j]
    return bag[n][maxW]
n=int(input("Enter no. of item: "));
maxW=int(input("Enter maximum capacity: "));
W=[0];
P=[0];
for i in range (n):
    W.append(int(input("Enter weight: ")));
    P.append(int(input("Enter price: ")));
value= knapsack(n,maxW,W,P);
print("Maximum value of bag: ",value);
