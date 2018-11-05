import msvcrt
while True:
    if msvcrt.kbhit():
        break
    else:
        print("pass")
print("done")
