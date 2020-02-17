list = list(int(input()) for i in range(4))
print(list[0]*list[2] if list[0] <= list[1] else list[1] * list[2] + (list[0] - list[1]) * list[3])
