S=input()
list = list(int(S[i:i+3]) for i in range(len(S)-2))
result = min(abs(i-753) for i in list)
print(result)
