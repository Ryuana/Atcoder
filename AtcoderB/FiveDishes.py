import math

list=list((int(input()) for i in range(5)))
min=10
index=0
result=0
for i in range(len(list)):
    if min > list[i]%10 and list[i]%10 !=0:
        min=list[i]%10
        index=i
for i in range(len(list)):
    if i != index:
        result+=math.ceil(list[i]/10)*10
result+=list[index]
print(result)
