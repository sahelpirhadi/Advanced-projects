adad=input()
adad_list=adad.split("+")
new_adad=""
adad_list=sorted(adad_list)
for i in adad_list:
    new_adad=new_adad+i+"+"
new_adad=new_adad.strip("+")
print(new_adad)
