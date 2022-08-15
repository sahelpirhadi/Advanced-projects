n=int(input())
loghatname={}
for i in range(0,n):
    kalame=input()
    list_kalame=kalame.split()
    loghatname[list_kalame[0]]=list_kalame[1]
jomle=input()
new=''
for i in jomle.split():
    if i in loghatname:
        new=new+loghatname[i]+' '
    else:
        new=new+i+' '
jomle.strip()
print(new)
    
    
