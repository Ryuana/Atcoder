N=int(input())
set=set()
bool=True
list = (list(input()for i in range(N)))
    # S=input()
    # if S in set or :
    #     bool=False
    #     break
set.add(list[0])
for i in range(1,N):
    if list[i] in set or list[i-1][-1] != list[i][0]:
        bool=False
        break
    set.add(list[i])
print('Yes' if bool else 'No')
