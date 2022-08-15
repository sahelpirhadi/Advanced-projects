adad=int(input())
count=0
for i in range(1,adad+1):
    if adad%i==0:
        count=count+1
if count==2 or adad==2:
    print("prime")
else:
    print("not prime")
