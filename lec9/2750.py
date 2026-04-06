turn=int(input())
N=[int(input()) for i in range(turn)]
N.sort()
for i in range(len(N)):
    print(N[i])
