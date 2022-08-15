jomle=input()
sedadar="aeiou"
jadid=""
jomle=jomle.lower()
for i in jomle:
    if i in sedadar:
        jomle.replace(i,"")
    else:
        jadid=jadid+"."+i
print(jadid)
