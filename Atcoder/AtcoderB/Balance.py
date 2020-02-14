N=int(input())
list=list(map(int,input().split()))
sum=sum(list)
cnt=0
for i in range(N):
    cnt+=list[i]
    if cnt >=sum/2:
        sa=sum-cnt
        kotae=cnt-sa
        cnt=cnt-list[i]
        sa=sum-cnt
        kotae2=sa-cnt
        if kotae < kotae2:
            print(kotae)
        else:
            print(kotae2)
        break
