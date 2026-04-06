turn=int(input())
PS=[]
for i in range(turn):
    PS.append(list(input()))

def isitno(pslist):
    stack=[]
    
    for char in pslist:
        if char=='(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                return
    if not stack:
        print('YES')
    else:
        print('NO')
      
for i in range(turn):
    isitno(PS[i])
