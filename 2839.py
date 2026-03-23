weight = int(input())
bags = 0

while weight >= 0: #keep /5 and -3 to use less 3kg bags
    if weight % 5 == 0:    
        bags += (weight // 5)
        print(bags)
        break
    weight -= 3           
    bags += 1
else:                     
    print(-1)
