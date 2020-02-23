N = int(input())
result = 0
X = list(map(int,input().split()))
P = round(sum(X)/N+0.01)
for i in range(N):
    result += abs(X[i]-P)**2
print(result)
