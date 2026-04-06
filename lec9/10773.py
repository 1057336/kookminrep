turn=int(input())
numbers=[]
for i in range(turn):
    inputnum=int(input())
    if inputnum :
        numbers.append(inputnum)
    else:
        numbers.pop()
print(sum(numbers))
