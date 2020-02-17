N=int(input())
print(int(N/2) if N%2==0 else int(N/2+1))
for i in range(int(N/2)):
    print(2)
if(N%2==1):
    print(1)
