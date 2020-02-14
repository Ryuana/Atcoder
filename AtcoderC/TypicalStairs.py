N,M=map(int,input().split())
list=[0]*M
list[0]=int(input())
bool=True
for i in range(1,N):
    list[i] = int(input())
    if list[i]-list[i-1] >=1:
        bool=False
        break
if bool:
    
else:
    print(0)
