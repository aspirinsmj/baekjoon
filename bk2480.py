a,b,c = map(int, input().split())
if a==b==c:
    print("%d"%(10000+(a*1000)))
elif a==b or b==c:
    print("%d"%(1000+b*100))
elif a==c:
    print("%d"%(1000+c*100))
else:
    print("%d"%(100*max(a,b,c)))