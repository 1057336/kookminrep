n=int(input())
x=list(map(int,input().split()))
x.sort()

Nsum=0
for i in range(n):
    Nsum += (i - (n - 1 - i)) * x[i]
        
print(Nsum*2)
