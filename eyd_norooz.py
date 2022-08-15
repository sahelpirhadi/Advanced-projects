adad=input()
y=[]
adad2=adad.split()
for x in adad2:
    y.append(int(x))
y.sort()
z=y[-1]-y[0]
print(z)
