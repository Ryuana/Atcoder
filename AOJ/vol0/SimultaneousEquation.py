def keisan(a,b,c,d,e,f):
    if a*d-b*c!=0:
        x=(c*e-b*f)/(a*e-b*d)
        y=(a*f-c*d)/(a*e-b*d)
    if x == 0:
        x=0
    elif y == 0:
        y=0
    # if a!=0:
    #     cross=d/a
    # else:
    #     cross=0
    # if (b*cross-e)!=0:
    #     y=(c*cross-f)/(b*cross-e)
    # else:
    #     y=0
    # if (-1*b*y+c)+(-1*e*y+f) !=0:
    #     x=(a+d)/((-1*b*y+c)+(-1*e*y+f))
    # else:
    #     x=0
    print("{0:.3f}".format(round(x,4)),"{0:.3f}".format(round(y,4)))
while True:
    try:
        a,b,c,d,e,f=map(int,input().split())
        keisan(a,b,c,d,e,f)
    except:break
