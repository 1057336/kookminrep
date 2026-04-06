N=int(input())
count=1
for i in range(2,10):
    newN=int(input())
    if newN>N:
        N=newN
        count=i
print(N)
print(count)
