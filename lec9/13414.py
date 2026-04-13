input = open(0).readline
line1 = input().split()
if line1:
    N, M = map(int, line1)
    students = {}

    for _ in range(M):
        idnumber = input().strip()
        if not idnumber:
            continue
        if idnumber in students:
            del students[idnumber]
        students[idnumber] = True

    result = list(students.keys())
    count = 0
    for i in range(len(result)):
        if count == N:
            break
        print(result[i])
        count += 1
