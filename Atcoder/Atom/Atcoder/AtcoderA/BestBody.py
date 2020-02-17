N,S,T = map(int,input().split())
list = list(int(input())for i in range(N))
weight = list[0]
cnt = 0
if weight >= S and weight <=T:
    cnt+=1
for i in range(1,N):
    weight +=list[i]
    if weight >= S and weight <=T:
        cnt +=1
print(cnt)
