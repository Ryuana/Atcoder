N,M,C=map(int,input().split())
B=list(map(int,input().split()))
sum=0
cnt=0
for i in range(N):
    A=list(map(int,input().split()))
    for j in range(M):
        sum+=A[j]*B[j]
    if sum + C > 0:
        cnt+=1
    sum=0
print(cnt)
