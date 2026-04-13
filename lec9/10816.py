N=int(input())
sgcard={}
sgcards=input().strip().split()
for card in sgcards:
    sgcard[card]=sgcard.get(card,0)+1
M=int(input())
Mcards=input().strip().split()

print(*(sgcard.get(card, 0) for card in Mcards))
