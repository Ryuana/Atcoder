N=int(input())
list=list(map(int,input().split()))
while len(list) != 0and max(list) > len(list):
    list = [i for i in list if i < len(list)]
#list2 = [i for i in list if i < N]
set = set(list)
cnt=0
for i in set:
    c=list.count(i)
    if c > i:
        cnt +=c-i
    elif c < i:
        cnt +=c
print(N-len(list)+cnt)
