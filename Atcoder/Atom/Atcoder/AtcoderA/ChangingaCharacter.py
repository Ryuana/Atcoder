N,K=map(int,input().split())
S=input()
result=''
for i in range(N):
    if i != K-1:
        result+=S[i]
    else:
        result+=S[i].lower()
print(result)
