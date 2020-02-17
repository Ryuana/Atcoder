list=list(map(int,input().split()))
list.sort()
print('Yes' if list[2] == list[0] + list[1] else 'No')
