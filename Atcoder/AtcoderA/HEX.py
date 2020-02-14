a=['A','B','C','D','E','F']
X,Y=input().split()
print('=' if a.index(X) == a.index(Y) else '<' if a.index(X) < a.index(Y) else '>')
