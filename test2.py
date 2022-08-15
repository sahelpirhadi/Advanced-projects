import hashlib
import csv
def hash_password_hack(input_file_name, output_file_name):
     hash_password_to_password={}
     n=[]
     for password in range(1000,10000):
          hashing_number=hashlib.sha256(b'%i'%password).hexdigest()
          hash_password_to_password[hashing_number]=password
     with open(input_file_name) as f:
          reader=csv.reader(f)
          for row in reader:
               t=[]
               t.append(row[0])
               password2=hash_password_to_password[row[1]]
               t.append(password2)
               n.append(t)
     with open(output_file_name,'w',newline='') as fin:
          writer=csv.writer(fin)
          writer.writerows(n)
