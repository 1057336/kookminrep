A,B= map(int,input().split())
#반 접어서 계산
if A<B :
    temp=A
    A=B
    B=temp
print( ((A+B) *(A-B+1)) //2)