N=int(input())
list=list()
cnt=0
for i in range(105,N+1,2):
    list=[j for j in range(1,200)if i%j<1]
    if len(list) >=8:
        cnt+=1
print(cnt)
