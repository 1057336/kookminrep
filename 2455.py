people=list(map(int, input().split()))
for i in range(3) :
    people.extend(list(map(int, input().split())))
max=0
train=0;
for i in range(8) :
    if (i%2) :
        train+=people[i]
    else :
        train-=people[i]
    if train>max : 
        max=train
print(max)
