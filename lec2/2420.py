N,M=input().split()
N=int(N)
M=int(M)
if N<M :
 a=M
 M=N
 N=a 

if N<0: 
    print (N-M)
else : 
    print((M-N)*-1)

 