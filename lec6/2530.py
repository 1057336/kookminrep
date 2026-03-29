h,m,s=map(int, input().split())
howlong=int(input())
s+=(howlong%60)
m+=((howlong//60)%60)
h+=(((howlong//60)//60)%24)

if s>=60 :
    m+=1
    s= s%60
if m>=60 :
    h+=1
    m= m%60
if h>=24 :
    h= h%24
    
print(f'{h} {m} {s}')
