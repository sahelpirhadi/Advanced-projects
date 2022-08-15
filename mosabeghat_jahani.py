list_of_goals=[]
globall={}
sorted_match=[['Iran','Spain'],['Iran','Portugal'],['Iran','Morocco'],['Spain','Portugal'],
              ['Spain','Morocco'],['Portugal','Morocco']]
for i in range(0,6):
    z=input().split("-")
    list_of_goals.append([int(z[0]),int(z[1])])
for j in range(0,6):
    for k in range(0,2):
        y=0
        y=list_of_goals[j][k]-list_of_goals[j][k-1]
        if sorted_match[j][k]  not in globall.keys():
            globall[sorted_match[j][k]]=globall.get(sorted_match[j][k],[0,0,0,y,0])
        else:
            globall[sorted_match[j][k]][3]=globall[sorted_match[j][k]][3]+y
for q in range(0,6):
    if list_of_goals[q][0]>list_of_goals[q][1]:
        globall[sorted_match[q][0]][0]=globall[sorted_match[q][0]][0]+1
        globall[sorted_match[q][0]][4]=globall[sorted_match[q][0]][4]+3
        globall[sorted_match[q][1]][1]=globall[sorted_match[q][1]][1]+1
    elif list_of_goals[q][0]==list_of_goals[q][1]:
        globall[sorted_match[q][0]][2]=globall[sorted_match[q][0]][2]+1
        globall[sorted_match[q][1]][2]=globall[sorted_match[q][1]][2]+1
        globall[sorted_match[q][0]][4]=globall[sorted_match[q][0]][4]+1
        globall[sorted_match[q][1]][4]=globall[sorted_match[q][1]][4]+1
    else:
        globall[sorted_match[q][1]][0]=globall[sorted_match[q][1]][0]+1
        globall[sorted_match[q][0]][1]=globall[sorted_match[q][0]][1]+1
        globall[sorted_match[q][1]][4]=globall[sorted_match[q][1]][4]+3
final=list(globall.items())
sorted_list=sorted(final, key=lambda x:(-x[1][4],-x[1][0],x[0]))
for m in sorted_list:
    print('{}  wins:{} , loses:{} , draws:{} , goal difference:{} , points:{}'.format(m[0],m[1][0],m[1][1],m[1][2],m[1][3],m[1][4]))
