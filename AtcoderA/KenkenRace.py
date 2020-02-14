N,A,B,C,D=map(int,input().split())
S=input()
try:
    S.index('##')
    print('No')
except:
    try:
        S.index('...')
        print('Yes')
    except:
        if C > D:
            if S[D-2] == '#' or S[D] == '#':
                print('No')
            else:
                print('Yes')
        else:
            print('Yes')
