import requests
import mysql.connector
from bs4 import BeautifulSoup
name=input()
cnx=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='sahel')
cursor=cnx.cursor()
r=requests.get('https://www.truecar.com/used-cars-for-sale/listings/%s/'%(name))
soup=BeautifulSoup(r.text,'html.parser')
val2=soup.find_all('div',attrs={'data-test':'vehicleCardPricingBlockPrice'})
val3=soup.find_all('span',attrs={'class':'vehicle-header-make-model text-truncate'})
val4=soup.find_all('div',attrs={'data-test':'vehicleMileage'})
for i in range(0,20):
    a=val3[i].contents[0]+val3[i].contents[4]
    b=val2[i].contents[0]
    c=val4[i].contents[-3]
    cursor.execute('insert into truecar values(\'%s\',\'%s\',\'%s\')'%(a,b,c))
cnx.commit()
cnx.close()
