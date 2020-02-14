N,M,X,Y=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
Z=min(y) if min(y) < Y else Y
if max(x) < Z and X < Z:
    print('No War')
else:
    print('War')
