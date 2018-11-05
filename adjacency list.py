n=int(input("Enter no of vertices: "))
graph={}
for i in range(n):
    node=input("Enter name of vertex")
    graph[node]=[]
for i in graph:
    n=int(input("Enter no of edges of %s node "%i))
    for i in range(m):
        adj=int(input("Enter the adjecent vertex name:"))
        if adj in graph:
            graph[i].append(adj)
        else:
            break
            print(graph)
