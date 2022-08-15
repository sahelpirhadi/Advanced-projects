tedad_bazikonan=int(input())
dafaate_jahani=input()
count=0
dafaate_jahani2=dafaate_jahani.split()
for i in range(0,tedad_bazikonan):
    dafaate_jahani2[i]=int(dafaate_jahani2[i])
    if dafaate_jahani2[i]<=2:
        count=count+1
tedad_goroh=count//3
        
print(tedad_goroh)
