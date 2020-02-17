A,B,K=map(int,input().split())
ans = list()
for i in range(1,10001):
    if A%i == 0 and B%i == 0:
        ans.append(i)
print(ans[-K])
