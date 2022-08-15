import mysql.connector
import re
regex=r'\b[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'
email=input()
password=input()
while (re.fullmatch(regex,email))==None:
    print('correct=expression@string.string')
    email=input()
    password = input()
cnx=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='sahel')
cursor=cnx.cursor()
cursor.execute(('INSERT INTO email VALUES (%s,%s);'),(email,password))
cnx.commit()
cnx.close()
