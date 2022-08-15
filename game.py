import random
hads=random.randint(1,99)
print(hads)
javab=input("is that true?")
mini=1
maxi=99
while javab!="d":
    if javab=="k":
        maxi=hads-1
        hads=random.randint(mini,maxi)
        print(hads)
    elif javab=="b":
        mini=hads+1
        hads=random.randint(mini,maxi)
        print(hads)
    javab=input("is that true?")
print("yeey the answer was",hads,"!")
                
            
