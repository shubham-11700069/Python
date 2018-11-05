graph={'a':['b','c','d'],'b':['c','e'],'c':['f'],'d':['c','g'],'e':['h'],'f':['c','g'],'g':['h'],'h':[]}
status={}
for i in graph:
    status[i]=0
stack=[]
root=input("Enter root element: ")
stack.append(root)
status[root]=1
while len(stack)!=0:
    element=stack[len(stack)-1]
    print(element)
    status[element]=2
    del stack[len(stack)-1]
    for i in graph[element]:
        if status[i]==0:
            stack.append(i)
            status[i]=1

        
