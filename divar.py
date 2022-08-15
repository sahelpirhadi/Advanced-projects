import requests
from bs4 import BeautifulSoup
r=requests.get('https://divar.ir/s/tehran')
soup=BeautifulSoup(r.text,'html.parser')
val=soup.find_all('div',attrs={'class':'kt-post-card__body'})
for i in val:
    val2=i.find_all('div',attrs={'class':'kt-post-card__description'})
    if val2!=[]:
        if val2[0].contents[0].find('توافقي')!=-1:
            val3=i.find_all('div',attrs={'class':'kt-post-card__title'})
            print(val3)
        else:
             continue
        
    
        
        

