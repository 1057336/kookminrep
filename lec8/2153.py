#a=97 ->1
#A=65 ->27
import math

word=list(input())
wordnum=0
for i in range(len(word)):
    word[i]=ord(word[i])


for i in range(len(word)):
    if word[i]>=97 and word[i]<=123 :
        wordnum+=(word[i]-96)
    elif word[i]>=65 and word[i]<=91:
        wordnum+=(word[i]-38)
if wordnum<2:
    print('It is a prime word.')
    exit(0)

for i in range (2, int(math.sqrt(wordnum)) + 1):
    if wordnum%i ==0 :
        print("It is not a prime word.")
        exit(0)
print('It is a prime word.')