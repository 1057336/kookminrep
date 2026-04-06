n=int(input())
x=list(map(int,input().split()))
Nsum=0
for i in range(n):
    for j in range(n):
        Nsum+=abs(x[i]-x[j])
print(Nsum)
