N,M=map(int,input().split())
ans = [0] * M
cnt=0
for i in range(N):
    A = list(map(int,input().split()))
    for j in range(1,A[0]+1):
         ans[A[j]-1] +=1
for i in range(M):
    if ans[i] == N:
        cnt +=1
print(cnt)
