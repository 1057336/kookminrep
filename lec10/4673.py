allnumset = set(range(1, 10001))
newnumset= set()

def d(n):
    result = n
    for number in str(n):
        result = result+int(number)
    return result


for i in range(1, 10001):
    newnum = d(i)
    if newnum <= 10000:
        newnumset.add(newnum)

selfnums = sorted(allnumset - newnumset)
#차집합

for i in selfnums:
    print(i)
