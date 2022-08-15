final=[]
for i in range(0,10):
    adad=int(input())
    b=0
    for j in range(1,adad+1):
        if adad%j==0:
            a=0
            for x in range(1,j+1):
                if j%x==0:
                    a=a+1
            if a==2:
                b=b+1
    final.append((adad,b))
sorted_list=sorted(final, key=lambda x:(x[1],x[0]))
print(sorted_list[-1][0],sorted_list[-1][1])
        
                    
