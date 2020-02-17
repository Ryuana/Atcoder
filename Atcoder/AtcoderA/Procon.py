result=0
for i in range(3):
    a,b = map(int,(input().split()))
    result+=a*b/10
print(int(result))
