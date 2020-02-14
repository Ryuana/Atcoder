import math
list=list(map(int,input().split()))
txa=list[0]
tya=list[1]
txb=list[2]
tyb=list[3]
T=list[4]
V=list[5]
n=int(input())
bl=False
for i in range(n):
    x,y=map(int,input().split())
    if T*V >=(math.sqrt((x-txa)**2 + (y-tya)**2) + math.sqrt((txb-x)**2 + (tyb-y)**2)):
        bl=True
        break
if bl == True:
    print('YES')
else:
    print('NO')
