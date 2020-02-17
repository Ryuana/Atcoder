N=int(input())
T,A=map(int,input().split())
list=list(map(int,input().split()))
tmp=10**5
for i in range(N):
    if tmp > abs(T-list[i]*0.006-A):
        tmp = abs(T-list[i]*0.006-A)
        index=i+1
print(index)
