a,b= input().split(" ")
a= int(a)
b= int(b)

if b>=45:
    b-=45
    print("%d %d"%(a,b))
elif b<45:
    if a==0:
        a=23
        print("%d %d"%(a,60+(b-45)))
    else:
        a-1
        print("%d %d"%(a-1,60+(b-45)))