N=int(input())
ans = 0
for i in range(N):
    x1,u1=input().split()
    if u1 == 'JPY':
        ans += float(x1)
    else:
        ans += float(x1)*380000
print(ans)
