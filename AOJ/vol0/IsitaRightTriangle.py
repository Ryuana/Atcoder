N=int(input())
for i in range(N):
    x,y,z=sorted(list(map(int,input().split())))
    if x**2 + y**2 == z**2:
        print('YES')
    else:
        print('NO')
