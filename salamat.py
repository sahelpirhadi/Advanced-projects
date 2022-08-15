class student:
    def __init__(self,tedad,sen,ghad,vazn):
        self.sen=sen.split(" ")
        for i in range(0,len(self.sen)):
            self.sen[i]=int(self.sen[i])
        self.ghad=ghad.split(" ")
        for j in range(0,len(self.ghad)):
            self.ghad[j]=int(self.ghad[j])
        self.vazn=vazn.split(" ")
        for k in range(0,len(self.vazn)):
            self.vazn[k]=int(self.vazn[k])
        self.tedad=tedad
    def khoroji(self):
        import numpy
        self.meansen=numpy.mean(self.sen)
        self.meanghad=numpy.mean(self.ghad)
        self.meanvazn=numpy.mean(self.vazn)
        return(self.meansen,self.meanghad,self.meanvazn)

s='AB'
final=[]
for i in s:
    out=[]
    tedad=int(input())
    sen=input()
    ghad=input()
    vazn=input()
    i=student(tedad,sen,ghad,vazn)
    out=i.khoroji()
    for i in out:
        print(i)
    final.append(out)
if final[0][1]>final[1][1]:
    print('A')
elif final[0][1]<final[1][1]:
    print('B')
elif final[0][1]==final[1][1] and final[0][2]<final[1][2]:
    print('A')
elif final[0][1]==final[1][1] and final[0][2]>final[1][2]:
    print('B')
else:
    print('Same')
    
    
