N=int(input())
bool=False
for i in range(0,N+1,4):
    for j in range(i,N+1,7):
        if j == N:
            bool = True
            break
if bool and N!=0:
    print('Yes')
else:
    print('No')
