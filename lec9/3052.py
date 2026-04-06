N=[(int(input())%42) for i in range(10)]
diffrent=[N[0]]
for i in range(1,10):
    for j in range(len(diffrent)):
        if N[i] not in diffrent:
            diffrent.append(N[i])
print(len(diffrent))
