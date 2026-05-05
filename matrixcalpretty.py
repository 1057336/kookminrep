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
    
n=int(input("input number (2~5): "))

if 1 < n <= 5:
    A = createmat(n)
    B = createmat(n)
    C = createmat(n)

    printmat(A, "Matrix A")
    printmat(B, "Matrix B")
    printmat(C, "Matrix C")


    mul_result = []
    for i in range(n):
        mul_result.append([0] * n)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                mul_result[i][j] += A[i][k] * B[k][j]


    finalresult = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(mul_result[i][j] + C[i][j])
        finalresult.append(row)

    printmat(finalresult, "Result (A * B + C)")
        
