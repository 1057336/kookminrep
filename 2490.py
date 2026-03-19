#도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E
yut1=list(map(int,input().split()))
yut2=list(map(int,input().split()))
yut3=list(map(int,input().split()))

def yutnori(yutbatch):
    count=0
    for i in range(4) :
        if yutbatch[i] == True :
            count+=1
    if count ==1 :
        print("C")
    elif count ==2 :
        print("B")
    elif count ==3 :
        print("A")
    elif count ==4 :
        print("E")
    else :
        print("D")
        
yutnori(yut1)
yutnori(yut2)
yutnori(yut3)
