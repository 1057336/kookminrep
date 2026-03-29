N,K=map(int,input().split())
maxnum=N
for i in range(1,K+1):
    reverse=((N*i)%10*10 + (N*i)//10)
    if maxnum<reverse :
        maxnum=reverse
print(maxnum)