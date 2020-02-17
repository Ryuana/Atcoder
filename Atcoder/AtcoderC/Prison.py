N,M=map(int,input().split())
set1=set()
# set2=set()
L,R=map(int,input().split())
for i in range(L,R+1):
    set1.add(i)
min=min(set1)
max=max(set1)
Flag=True
for i in range(M-1):
    L,R=map(int,input().split())
    if R < min:
        Flag=False
        break
    elif L > max:
        Flag=False
        break
    if L >= min and max >= L:
        min = L
    if R >= min and max >= R:
        max = R
    # if min <= L:
    #     min=L
    # if max >= R+1:
    #     max=R+1
    # for j in range(min,max):
    #     set2.add(j)
    # set1=set1&set2
    # set2.clear()
if Flag:
    print(max-min+1)
else:
    print(0)
