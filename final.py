import requests
import mysql.connector
from bs4 import BeautifulSoup
from sklearn import tree
esm=input("insert name:")
kilometr=input("insert mileage:")
sal=input("insert year:")
cnx=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='sahel')
cursor=cnx.cursor()
summ=0
for i in range(1,21):
    val2=[]
    val3=[]
    val4=[]
    val5=[]
    if i==1:
        r=requests.get('https://www.truecar.com/used-cars-for-sale/listings/')
        soup=BeautifulSoup(r.text,'html.parser')
        val2=soup.find_all('div',attrs={'data-test':'vehicleCardPricingBlockPrice'})
        val3=soup.find_all('span',attrs={'class':'vehicle-header-make-model text-truncate'})
        val4=soup.find_all('div',attrs={'data-test':'vehicleMileage'})
        val5=soup.find_all('span',attrs={'class':"vehicle-card-year font-size-1"})
    else:
        r=requests.get('https://www.truecar.com/used-cars-for-sale/listings/?page=%s'%(str(i)))
        soup=BeautifulSoup(r.text,'html.parser')
        val2=soup.find_all('div',attrs={'data-test':'vehicleCardPricingBlockPrice'})
        val3=soup.find_all('span',attrs={'class':'vehicle-header-make-model text-truncate'})
        val4=soup.find_all('div',attrs={'data-test':'vehicleMileage'})
        val5=soup.find_all('span',attrs={'class':"vehicle-card-year font-size-1"})
    for j in range(0,len(val2)):
        a=val3[j].contents[0]+val3[j].contents[4]
        b=val2[j].contents[0]
        c=val4[j].contents[-3]
        d=val5[j].contents[0]
        summ+=1
        cursor.execute('insert ignore into ml values(\'%s\',\'%s\',\'%s\',\'%s\')'%(a.lower(),b,c,d))
cnx.commit()
query='SELECT DISTINCT * FROM ml where Name=\'%s\';'%(esm)
cursor.execute(query)
x=[]
y=[]

for (name,price,mileage,year) in cursor:
    x.append([int(mileage.replace(',','')),int(year)])
    y.append([int(price[1:].replace(',',''))])
cnx.close()

clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
new_data=[[int(kilometr),int(sal)]]
answer=clf.predict(new_data)
print(answer[0])
