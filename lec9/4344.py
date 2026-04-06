turn=int(input())
cases=[list(map(int,input().split())) for i in range(turn)]
#cases[i][0] = student count

for i in range(turn):
    avg=(sum(cases[i][1:cases[i][0]+1]))/cases[i][0]
    
    over=0
    for j in range(1,cases[i][0]+1):
        if avg<cases[i][j]:
            over=over+1
    print(f'{round(over/cases[i][0]  * 100,3)}%')
print()

