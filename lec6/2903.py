N=int(input())
#  1=>3*3, 2=>5*5.. 
#increasing with +1,2,4,8... 2^N-1 
result=2

for i in range (N) :
    result+= 2**i
    #print(f'{i+1} spin {result}')
    
#print( f'result {result}')
print(result**2)
