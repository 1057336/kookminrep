turn=int(input())
a=[0]*turn
b=[0]*turn
for i in range(turn) :
    a[i],b[i]=map(int,input().split())
for i in range(turn) :
    print(f'Case #{i+1}:',a[i]+b[i])
    