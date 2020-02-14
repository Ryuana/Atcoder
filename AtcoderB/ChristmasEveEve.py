N=int(input())
list=list(int(input()) for i in range(N))
print(sum(list)-int(max(list)/2))
