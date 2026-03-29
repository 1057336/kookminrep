sang=int(input())
jung=int(input())
ha=int(input())
cola=int(input())
cidar=int(input())

minburger = sang
if jung<ha:
    if minburger>jung :
        minburger=jung
elif minburger>ha :
    minburger=ha

if cola<cidar : 
    print(minburger+cola-50)
else :
    print(minburger + cidar-50)