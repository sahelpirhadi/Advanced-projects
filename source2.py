import csv
# For the average
from statistics import mean 
def calculate_averages(input_file_name,output_file_name):
    with open(input_file_name)as f:
        reader=csv.reader(f)
        n=[]
        for row in reader:
            new=[]
            adad=[]
            new.append(row[0])
            for number in row[1:]:
                adad.append(int(number))
            miangin=mean(adad)
            new.append(str(miangin))
            n.append(new)
            with open(output_file_name,'w',newline='') as fin:
                writer=csv.writer(fin)
                writer.writerows(n)
def calculate_sorted_averages(input_file_name, output_file_name):
    my_dict={}
    with open(input_file_name)as f:
        reader=csv.reader(f)
        for row in reader:
            adad=[]
            for number in row[1:]:
                adad.append(int(number))
            miangin=mean(adad)
            my_dict[row[0]]=str(miangin)
            new=my_dict.items()
        sorted_list=sorted(new, key=lambda x:(float(x[1]),x[0]))
    with open(output_file_name,'w',newline='') as fin:
        writer=csv.writer(fin)
        writer.writerows(sorted_list)
def calculate_three_best(input_file_name, output_file_name):
    my_dict={}
    with open(input_file_name)as f:
        reader=csv.reader(f)
        for row in reader:
            adad=[]
            for number in row[1:]:
                adad.append(int(number))
            miangin=mean(adad)
            my_dict[row[0]]=str(miangin)
            new=list(my_dict.items())
        sorted_list=sorted(new, key=lambda x:(float(x[1]), x[0]))
        sorted_list.reverse()
        with open(output_file_name,'w',newline='') as fin:
            writer=csv.writer(fin)
            writer.writerows(sorted_list[:3])
def calculate_three_worst(input_file_name, output_file_name):
    my_dict={}
    just_number=[]
    with open(input_file_name)as f:
        reader=csv.reader(f)
        for row in reader:
            adad=[]
            for number in row[1:]:
                adad.append(int(number))
            miangin=mean(adad)
            my_dict[row[0]]=str(miangin)
            new=list(my_dict.items())
        sorted_list=sorted(new, key=lambda x:(float(x[1]), x[0]))
        for i in range(0,len(sorted_list)):
            just_number.append(sorted_list[i][1])
        with open(output_file_name,'w',newline='') as fin:
            writer=csv.writer(fin,delimiter=' ')
            writer.writerows(just_number)
def calculate_average_of_averages(input_file_name, output_file_name):
     my_dict={}
     miangins=[]
     new2=[]
     with open(input_file_name)as f:
        reader=csv.reader(f)
        for row in reader:
            adad=[]
            for number in row[1:]:
                adad.append(int(number))
            miangin=mean(adad)
            my_dict[row[0]]=str(miangin)
            new=list(my_dict.items())
        for j in range(0,len(new)):
            miangins.append(float(new[j][1]))
        miangin_of_miangins=mean(miangins)
        with open(output_file_name,'w',newline='') as fin:
            writer=csv.writer(fin, delimiter=' ')
            writer.writerow(str(miangin_of_miangins))

calculate_average_of_averages()
