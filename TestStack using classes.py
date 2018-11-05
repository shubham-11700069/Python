from stack import stack

Stack=stack()
for i in range(10):
    Stack.push(i)
while not Stack.isEmpty():
    print(Stack.pop(),end=" ")
