N,T=map(int,input().split())
c=[]
t=[]
result=[]
for i in range(N):
    S=input()
    c.append(int(S[0:S.find(' ')]))
    t.append(int(S[S.find(' ')+1:]))
for i in range(N):
    if t[i]<=T:
        result.append(c[i])
print(min(result) if len(result) != 0 else 'TLE')
