N=int(input())
list = list(map(int,input().split()))
print(['No','Yes'][max(list) < sum(list)-max(list)])
