S=int(input())
S1=S%100
S2=int(S/100)
if S1<=12 and S1!=0 and S2 <=12 and S2!=0:
    ans='AMBIGUOUS'
elif S1<=12 and S1!=0:
    ans='YYMM'
elif S2 <=12 and S2!=0:
    ans='MMYY'
else:
    ans='NA'
print(ans)
