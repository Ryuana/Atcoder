x,y=map(int,input().split())
Group=[1,2,1,3,1,3,1,1,3,1,3,1]
print('Yes' if Group[x-1] == Group[y-1] else 'No')
