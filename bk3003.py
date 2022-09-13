a = list(map(int,input().split(" ")))
b = [1,1,2,2,2,8]
c = []
i=0
while(i<6):
    if a[i]>=b[i]:
        c.append(-(a[i]-b[i]))
        i+=1
    else:
        c.append(b[i]-a[i])
        i+=1
print("%d %d %d %d %d %d"%(c[0],c[1],c[2],c[3],c[4],c[5]))