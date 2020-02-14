N = int(input())
print('Yes' if N%1000%111 == 0 or N%1110 < 10 else 'No')
