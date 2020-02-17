Primes = []
Primes.append(2)
for i in range(3,10000,2):
    check = 0
    for j in range(3,i+1,2):
        if i % j == 0:
            check += 1
            if check > 1:
                break
    if check == 1:
        Primes.append(i)
while True:
    try:
        cnt = 0
        n = int(input())
        for i in Primes:
            if n >= i:
                cnt+=1
            else:
                break
        print(cnt)
    except:break
