S=input()
max=0
for i in range(0,len(S)):
    if S[i] in ('A','C','G','T'):
        i+=1
        cnt=1
        while i<len(S) and S[i] in ('A','C','G','T'):
            i+=1
            cnt+=1
        if cnt > max:
            max=cnt
            cnt=0
print(max)
