import json
from urllib.request import urlopen
import requests
import  pprint
payload={'grant_type':'password',
         'username':'bankasa',
         'Password':'bangladesh'}
r=requests.post('http://training.finance.gov.bd/tcmapi/api/token',
               headers={"Authorization": "Basic QUNTOkFDU0Y0N0Q5QS1ES0E5LTBEMTItQjdCMC0wNEY0Mjc5QkJDQ1M=",
                        "Content-Type":"application/x-www-form-urlencoded"},data=payload)
r_dict=r.json()
#print(r_dict['access_token'])
print(r.json())