
#dijkstra's algorithm

graph=[[999,4,2,20],[4,999,999,3],[2,999,999,6],[20,3,6,999]]
src=[]
vertices=[]
destination=[]
distance=[]
D=0
S=int(input("enter source vetex :"));
dest=int(input("enter destination vertex :"));
n=len(graph[0]);
curr=S
while True:
    for i in range(n):
        if i not in vertices and graph[curr][i]!=999:
            distance.append(D +graph[curr][i]);
            src.append(curr)
            destination.append(i)
    if len(distance)>0:
        D=min(distance);
    vertices.append(curr);
    if dest in vertices:
        break;
    pos=distance.index(D);
    curr=destination[pos];
    del distance[pos]
    del src[pos]
    del destination[pos]
    print("minimum distance: ",D)
