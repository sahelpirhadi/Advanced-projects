import requests
from bs4 import BeautifulSoup
name=input()
r=requests.get('https://www.truecar.com/used-cars-for-sale/listings/%s/'%(name))
soup=BeautifulSoup(r.text,'html.parser')
val3=soup.find_all('span',attrs={'class':'vehicle-header-make-model text-truncate'})
for i in range(0,10):
    print(val3[i])
