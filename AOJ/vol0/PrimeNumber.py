#配列生成
Primes = [1]*1000001
#結果用配列
Result = []

for i in range(2,1000001,1):
    if Primes[i] == 1:
        for j in range(i+i,1000001,i):
            Primes[j] = 0
while True:
    try:
        Result.append(int(input()))
    except:
        break
for i in range(len(Result)):
    print(Primes[:Result[i]+1].count(1)-2)
