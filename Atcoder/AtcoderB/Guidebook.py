N=int(input())
Slist=list()
Plist=list()
tmp=list()
for i in range(N):
    S,P=input().split()
    Slist.append(S)
    Plist.append(int(P))
    tmp.append(int(P))
change = True
while change:
    change = False
    for i in range(len(Plist) - 1):
        if Plist[i] < Plist[i + 1]:
            Plist[i], Plist[i + 1] = Plist[i + 1], Plist[i]
            Slist[i], Slist[i + 1] = Slist[i + 1], Slist[i]
            change = True
print(Slist)
print(Plist)
change = True
while change:
    change = False
    for i in range(len(Slist) - 1):
        if Slist[i] > Slist[i + 1]:
            Slist[i], Slist[i + 1] = Slist[i + 1], Slist[i]
            Plist[i], Plist[i + 1] = Plist[i + 1], Plist[i]
            change = True
ans=list()
print(Slist)
print(Plist)
for i in range(N):
    ans.append(tmp.index(Plist[i]))
for i in range(N):
    print(ans[i]+1)
