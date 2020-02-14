W,H,x,y=map(int,input().split())
men=W*H/2
if x == 0 and y == 0:
    a=float(H/W)
else:
    if x == 0 and y != H:
        a=0
    elif x == 0 and y == H:
        a=float(H/W)
    else:
        a=float(y/x)
    if y == 0 and x ==W:
        a=float(H/W)
b=float(H/W)
W2=float(W/2)
H2=float(H/2)
cross=0
if a == b or x == W2 or y == H2:
    if a == b and x == W2:
        cross=1
    elif a == b and y == H2:
        cross=1
    elif x == W2 and y == H2:
        cross=1
    print("{0:.6f}".format(men),cross)
elif a > b:
    anx=float(H/a)
    men=(anx*H)/2
    print("{0:.6f}".format(men),cross)
else:
    any=float(W*a)
    men=(W*any)/2
    print("{0:.6f}".format(men),cross)
