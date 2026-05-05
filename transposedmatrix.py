import random

def createmat(n):
    matrix=[]
    
    limit=n*n*10
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(random.randint(1,limit-1))
        matrix.append(row)
        
    return matrix
    
    
def printmat(matrix,name):
    #pretty
    print(f"==={name}===")
    for i in range(len(matrix)): #in len so N
        row = matrix[i][:]
        for val in row:
            print(f"{val:>4}",end=" ")
        print()
    print()
    
def changeRowandCol(n):
    OGmat=createmat(n)
    printmat(OGmat,"Original matrix")
    
    CHmat=[]
    for i in range(n):
        newrow=[]
        for j in range(n):
            newrow.append(OGmat[j][i])
        CHmat.append(newrow)
        
    printmat(CHmat,"Transposed matrix")

n=int(input("input number (2~5): "))
if 1 < n <= 5:
    changeRowandCol(n)
else:
    print("try again, wrong number")
