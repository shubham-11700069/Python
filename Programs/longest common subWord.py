def lcw():
    u="secretery"
    v="secret"
    ste=[]
    lcw=[[0]*(len(v)+1) for x in range (len(u)+1)]
    maxl=0
    for c in range (len(v)-1,-1,-1):
        for r in range (len(u)-1,-1,-1):
            if u[r]==v[c]:
                lcw[r][c]=lcw[r+1][c+1]+1
                ste.append(u[r])
            else:
                lcw[r][c]=0
            if lcw[r][c]>maxl:
                maxl=lcw[r][c]
    return (maxl,ste)

print (lcw())

