import random
import time

NUMBER_OF_ELEMENTS=1000

lst=list(range(NUMBER_OF_ELEMENTS))
random.shuffle(lst)

s=set(lst)

startTime=time.time()
for i in range(NUMBER_OF_ELEMENTS):
    i in s

endTime=time.time()
runTime=int((endTime-startTime)*1000)
print("to test if",NUMBER_OF_ELEMENTS,"elements are in the set \n","runtime is",runTime,"miliseconds")

startTime=time.time()
for i in range(NUMBER_OF_ELEMENTS):
    i in lst

endTime=time.time()
runTime=int((endTime-startTime)*1000)
print("\n To test if",NUMBER_OF_ELEMENTS,"elements are in the list\n","runtime is",runTime,"miliseconds")

startTime=time.time()
for i in range(NUMBER_OF_ELEMENTS):
    s.remove(i)

endTim=time.time()
runTime=int((endTime-startTime)*1000)
print("\n To remove ",NUMBER_OF_ELEMENTS,"elements from the set\n","the runtime is: ",runTime,"miliseconds")

startTime=time.time()
for i in range(NUMBER_OF_ELEMENTS):
    lst.remove(i)

endTime=time.time()
runTime=int((endTime-startTime)*1000)
print("\n To remove ",NUMBER_OF_ELEMENTS,"elements from the list\n","the runtime is: ",runTime,"miliseconds")

