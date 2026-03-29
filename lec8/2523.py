turn=int(input())

for i in range(turn) :
    for j in range(i+1) :
        print('*',end='')
    print('')
for i in range(turn-1) :
    for j in range(turn-i-1) :
        print('*',end='')
    print('')
