import math
N,K = map(int,input().split())
start = K**int(math.log(N,K))
X = []
while start !=0:
    if N - start >= 0:
        N = N-start
        X.append(1)
    else:
        X.append(0)
    start = int(start / K)
print(len(X))
