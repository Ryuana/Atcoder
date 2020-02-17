while True:
    try:
        n=int(input())
        cnt=0
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        if i + j + k + l == n:
                            cnt+=1
        print(cnt)
        cnt=0
    except:break
