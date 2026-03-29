a=input()
sum=0
for i in range(5)  :
    sum+= pow(int(a.split()[i]), 2)
print(sum%10)