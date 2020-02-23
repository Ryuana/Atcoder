import numpy as np
#n種類,aとbが苦手
n,a,b = map(int,input().split())
array = [1]
tmp = array[0]
cnt = 0
for i in range(1,n+1,1):
    tmp *= i
    array.append(tmp)
print(array)
for i in range(1,n+1,1):
    if i == a or i == b:
        continue
    cnt += (array[n]/array[n-i])/array[i]
print(int(cnt%(1000000000+7)))
