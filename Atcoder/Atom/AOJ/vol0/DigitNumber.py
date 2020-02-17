a = []
b = []
while True:
    try:
        x,y=map(int,input().split())
        a.append(x)
        b.append(y)
    except:break
for i in range(len(a)):
    print(len(str(a[i]+b[i])))
