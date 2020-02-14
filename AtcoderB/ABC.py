S=input()
list = list(S)
cnt=0
while 'ABC' in S:
    n=S.index('ABC')
    list[n] = 'B'
    list[n+1] = 'C'
    list[n+2] = 'A'
    S=''.join(list)
    cnt+=1
print(cnt)
