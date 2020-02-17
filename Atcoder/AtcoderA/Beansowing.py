list=list(int(input()) for _ in range(3))
for i in range(3):
    print(3-sorted(list).index(list[i]))
