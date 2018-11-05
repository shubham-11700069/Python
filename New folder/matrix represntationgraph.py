n=int(input("Enter no of vertices: "))
graph=[[0]*n]*n
type=int(input("Enter 1 for weighted or 2 for unweighted graph: "))
if type==1:
    infinity=999
else:
    infinity=0
for i in range(n):
    for j in range(n):
        value=int(input("Is there any path in %d and %d: ."%(i,j)))
        if value==0:
            graph[i][j]=infinity
        if type==1 and value!=0:
            weight=int(input("Enter value of path: "))
            graph[i][j]=weight
        else:
            graph[i][j]=1
print("Enterd graph is: ")
for i in range(n):
    for j in range(n):
        print(graph[i][j],end='')
    print();
                
