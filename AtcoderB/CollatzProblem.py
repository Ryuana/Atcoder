s = int(input())
set = set([s])
cnt=1
while True:
    if s % 2 == 0:
        s = s/2
    else:
        s = s * 3 + 1
    cnt += 1
    if s in set:
        break
    set.add(s)
print(cnt)
