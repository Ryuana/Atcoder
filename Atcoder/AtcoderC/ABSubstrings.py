N=int(input())
start=0
end=0
r=0
cnt=0
for i in range(N):
    s=input()
    cnt+=s.count('AB')
    if s[0] == 'B':
        start+=1
    if s[-1] == 'A':
        end+=1
    if s[0] == 'B' and s[-1] == 'A':
        r+=1
if start == end and start == r and end > 0:
    cnt -=1
print(cnt+min(start,end))
