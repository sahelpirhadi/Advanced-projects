import mysql.connector
cnx=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='sahel')
cursor=cnx.cursor()
query='SELECT * FROM test'
cursor.execute(query)
mylist=[]
for (name,weight,height) in cursor:
    mylist.append([name,weight,height])
sorted_list = sorted(mylist, key=lambda x: (-x[2], x[1]))
for i in range(len(sorted_list)):
    print(sorted_list[i][0],sorted_list[i][1],sorted_list[i][2])
cnx.close()
