turn=int(input())
people=[]
for i in range(turn):
    peoplelog=input().split()
    if peoplelog[1]=='enter':
        people.append(peoplelog[0])
    elif peoplelog[1]=='leave'and peoplelog[0] in people:
        people.remove(peoplelog[0])
people.sort(reverse=True)
for i in range(len(people)):
    print(people[i])
