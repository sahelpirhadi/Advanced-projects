esm=input()
count=0
count2=0
for i in esm:
    if ord(i) in range(65,91):
        count=count+1
    else:
        count2=count2+1
if count>count2:
    esm=esm.upper()
else:
    esm=esm.lower()
print(esm)
