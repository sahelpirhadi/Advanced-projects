mydict={'f':[],'m':[]}
tedad=int(input())
for i in range(0,tedad):
    fard=input()
    listfard=fard.split(".")
    if listfard[0]=='f':
        mydict['f'].append((listfard[1].lower().capitalize(),listfard[2]))
    elif listfard[0]=='m':
        mydict['m'].append((listfard[1].lower().capitalize(),listfard[2]))
sorted_list1=sorted(mydict['f'], key=lambda x:(x[0]))
sorted_list2=sorted(mydict['m'], key=lambda x:(x[0]))
mydict['f']=sorted_list1
mydict['m']=sorted_list2
sorted_list3=sorted(mydict.items(), key=lambda x:(x[0]))
for j in range(0,2):
    for k in range(0,len(sorted_list3[j][1])):
        print(sorted_list3[j][0],sorted_list3[j][1][k][0],sorted_list3[j][1][k][1])
    
               
                   
