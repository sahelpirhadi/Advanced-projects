n=int(input())
reshte=""

import math
for i in range(0,n):
    new=""
    reshte=""
    listr=[]
    adad=int(input())
    rishe2=math.sqrt(adad)
    reshte=str(rishe2)
    listr=reshte.split(".")
    if listr[1]=='0':
        new=new+listr[0]+'.'+'0000'
    else:
        new=new+listr[0]+'.'+listr[1][:4]     
    print(new)
    
    
            
