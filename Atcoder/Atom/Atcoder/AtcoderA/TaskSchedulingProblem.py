Task = list(map(int,input().split()))
Task.sort(reverse = True)
print(Task[0] - Task[2])
