import json
from urllib.request import urlopen
import requests
import  pprint
payload={'UserID':"bafg@Buro",'Password':"baFG@&19Buro",'MemberCode':"0593100200",'BillDate':"02 Dec 2019"}
r=requests.get('http://gbanker.org:8111/Api/gBanker/GetCheckBill',
               headers={"Content-Type":"application/json"},json=payload)
r_dict=r.json()
print(r_dict['MemberName'])
#print(r.json())