import re
email=input()
res=re.search(r'.+\@.+\..+',email)
if res==None:
    print('WRONG')
else:
    print('OK')
