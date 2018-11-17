# -*- coding: utf-8 -*-
import requests

import requests.auth

# auth=requests.auth.HTTPBasicAuth("ryan","password")
#
# req=requests.post(url="http://pythonscraping.com/pages/auth/login.php",auth=auth)
# print(req.text)

url = 'https://api.ip2country.info/ip?13.8.13.76'
rep=requests.get(url,verify=False)
print(rep.json().get("countryName"))