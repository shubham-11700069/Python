class stack:
    def __init__(self):
        self.__elements=[]

    def isEmpty(self):
        if(len(self.__elements)==0):
            return 1
        else:
            return 0
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements[len(self.__elements)-1]

    def push(self,value):
        return self.__elements.append(value)

    def pop(self):
        if self.isEmpty==1:
            return ("list is empty")
        else:
            self.__elements.remove(len(self.__elements)-1)

            return ("item removed")

    def getSize(self):
        return len(self.__elements)
    def print(self):
        return (self.__elements)
