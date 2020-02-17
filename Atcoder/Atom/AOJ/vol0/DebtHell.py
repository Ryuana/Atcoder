import math
n=int(input())
ans=100000
for i in range(n):
    ans=math.ceil(ans*1.05/1000)*1000
print(ans)
