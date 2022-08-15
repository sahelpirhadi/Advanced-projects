import requests
import re
from bs4 import BeautifulSoup
r=requests.get('https://divar.ir/s/tehran')
soup=BeautifulSoup(r.text,'html.parser')
all_1=soup.find_all('div',attrs={'class':'kt-post-card__description'})
for i in all_1:
    s=i.contents
    res=re.search(r'تومان',s[0])
    print(res)
