matn=input()
final=[]
final2=[]
istrue=0
matn2=matn.split('.')
for i in matn2:
    i=i.strip()
    new=[]
    new=i.split(" ")
    final.append(new)
counter1=0
for k in range(len(final)):
    counter2=1
    for t in range(1,len(final[k])):
        
        if final[k][t].istitle()==True:
            istrue=istrue+1
            counter2=counter2+1
            print('{}:{}'.format(counter1+counter2,final[k][t].strip(".").strip(",")))
        
        else:
            counter2=counter2+1
    counter1=counter1+len(final[k])
if istrue==0:
    print(None)
