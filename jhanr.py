tedad=int(input())
mydict={'Horror':0,'Romance':0,'Comedy':0,'History':0,'Adventure':0,'Action':0}
for i in range(0,tedad):
    fard=input()
    listfard=fard.split(' ')
    for j in listfard[1:4]:
        mydict[j]=mydict[j]+1
sorted_list=sorted(mydict.items(), key=lambda x:(-x[1], x[0]))
for j in sorted_list:
    print('{} : {}'.format(j[0],j[1]))
        
