N,X=map(int,input().split())
list=list(map(int,input().split()))
sum=0
cnt=1
for i in range(N):
    sum+=list[i]
    if sum <=X:
        cnt+=1
    else:
        break
print(cnt)
