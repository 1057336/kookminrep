N=int(input())
if N<10:
    N=N*10
newNum=N
turn=0
while 1:
    turn=turn+1
    oldNum=newNum
    newNum=(oldNum%10)*10 + ((newNum//10)+ ((newNum%10)))%10
    if newNum==N :
        break;
print(turn)
