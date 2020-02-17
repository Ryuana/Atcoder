import math
while True:
    try:
        a,b=map(int,input().split())
        ans1=int(math.gcd(a,b))
        ans2=int(a*b/ans1)
        print(ans1,ans2)
    except:break
