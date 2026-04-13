N=int(input())
bookname={}

for _ in range(N):
    book = input().strip()
    if book in bookname:
        bookname[book] += 1
    else:
        bookname[book] = 1

booklist=list(bookname.items())
booklist.sort()
def getcount(item):
    return item[1]

booklist.sort(key=getcount,reverse=True)
print(booklist[0][0])

