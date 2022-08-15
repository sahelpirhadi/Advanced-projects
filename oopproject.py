class person:
    listafrad=[]
    def __init__(self,name):
        self.name=name
        person.listafrad.append(self.name)
class footbalist(person):
    def rndm(self):
        mydict={}
        import random
        d=['A','B']
        sum1=0
        sum2=0
        for i in person.listafrad:
            b=random.choice(d)
            if b=="A":
                sum1+=1
                if sum1!=11:
                    mydict[i]=b
                else:
                    mydict[i]="B"
            elif b=="B":
                sum2+=1
                if sum2!=11:
                    mydict[i]=b
                else:
                    mydict[i]="A"
            print(i,mydict[i])
        
    





a=footbalist("Hossein")
b=footbalist("Maziyar")
c=footbalist("Akbar")
d=footbalist("Nima")
e=footbalist("Mehdi")
f=footbalist("Farhad")
g=footbalist("Mohamad")
h=footbalist("Khashayar")
i=footbalist("Milad")
j=footbalist("Mostafa")
k=footbalist("Amin")
l=footbalist("Saeid")
m=footbalist("Pouya")
    n=footbalist("Pouria")
o=footbalist("Reza")
p=footbalist("Ali")
q=footbalist("Behzad")
r=footbalist("Soheil")
s=footbalist("Behrooz")
t=footbalist("Shahrouz")
u=footbalist("Saman")
v=footbalist("Mohsen")
v.rndm()
