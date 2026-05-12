def makedict(name:str):
    worddict={}
    f= open("Engdictionary.txt","r")
    for line in f:
        line=line.strip()
        if not line: 
            continue
        parts=line.split(maxsplit=1) 
        if len(parts)<2:
            continue
        #print(parts)

        tocken=parts[1].split(maxsplit=1)
        if len(tocken)<2:
            continue
        #print(tocken)
        word=tocken[0].strip()
        meaning=tocken[1].strip().strip('"')
        #qprint(f"{word} : {meaning}")
        worddict[word]=meaning
    return worddict


newdict=makedict("Engdictionary.txt")
#print(newdict)

print("------------English Dictionary------------")

while 1:
    
    print("\n> type [!quit] to exit")
    print("> type [!list] to exit")
    forsearch=input(" search >>")
    forsearch=forsearch.strip()
    forsearch="".join([forsearch[0].upper(),forsearch[1:].lower()])
    print()
    if forsearch == "!quit":
        break
    elif forsearch == "!list":
        for key in newdict:
            print(f"{key} : {newdict[key]}")
    elif forsearch in newdict:
        print(f">>{forsearch} :")
        print(f">>{newdict[forsearch]}")
    else:
        print(f">>{forsearch} is not in the dictionary")

print("\n------------Goodbye------------")
