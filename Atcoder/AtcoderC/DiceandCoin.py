import math
N,K=map(int,input().split())
J=math.ceil(math.log(K,2))
sum=0
cnt=1
for i in range(J,1,-1):
    start=int(K/(2**J))
    end=int(K/(2**(J-1)))
    sum+=float(N*((end-start)/(2**J)))
print(sum)
