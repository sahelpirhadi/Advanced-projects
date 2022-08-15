def my_final_grade_calculation(filename):
    handle=open(filename,'r')
    data=handle.readlines()
    mydict={}
    for i in data: 
        final=0
        i=i.strip().split(",")
        for j in range(1,len(i)):
            i[j]=int(i[j])
        empty=sorted(i[1:7])
        jam=0
        for z in empty[2:]:
            jam=jam+z
        miangin_q=jam/4
        empty2=sorted(i[7:11])
        jam2=0
        for m in empty2[1:]:
            jam2=jam2+m
        miangin_t=jam2/3
        for k in i[-2:]:
            final=final+k
        final=final+miangin_q+miangin_t
        final=final/4
        if final>=60:
            mydict[i[0]]=mydict.get(i[0],"pass")
        else:
            mydict[i[0]]="fail"
    print(mydict)

filename='my.txt'

my_final_grade_calculation(filename)
