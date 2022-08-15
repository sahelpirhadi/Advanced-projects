n=int(input())
adad3=[]
irsa=False
for i in range(0,n):
    adad=input()
    adad2=adad.split()
    for j in range(0,len(adad2)):
        adad2[j]=int(adad2[j])
    adad3.append(adad2)
i=0
while irsa==False and i<n:
    for j in range(1,n):
        if adad3[i][0]<adad3[j][0]:
            if adad3[i][1]>adad3[j][1]:
                print("happy irsa")
                irsa=True
                break
    i=i+1
                
if irsa==False:
    print("poor irsa")
