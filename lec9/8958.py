turn=int(input())
line=[0]*turn
for i in range(turn):
    line[i]=list(input())

for i in range(turn):
    count=0
    streak=0
    for j in range(len(line[i])):
        if line[i][j]=='O':
            count=count+1+streak;
            streak=streak+1
        else:
            streak=0
    print(count)
