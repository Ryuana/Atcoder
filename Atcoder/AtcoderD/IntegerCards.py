from scipy import stats
N,M=map(int,input().split())
list=list(map(int,input().split()))
list.sort()
for i in range(M):
    B,C=map(int,input().split())
    for j in range(C):
        if list[0] < B:
            if list[C-1] < B:
                for k in range(C):
                    list[j] = B
            else:
