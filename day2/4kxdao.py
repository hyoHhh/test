# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
f=open("科学刀资源杂烩.txt","w",encoding="utf-8")
cookie = ['97cd%2FwWKjqg%2FhDbvFGEOcIPDd2HtBfYAEeuodrGVxx%2FaBH4Mhrqh%2F6U2WRiD06SL4A57keh%2Fu41o5Y5PrUXJiNxbIQ	']
def get_a(url):
    s = requests.session()
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'content-encoding': 'gzip',
        'content-type': 'text/html; charset=utf-8',
        'date': 'Sun, 28 Oct 2018 23:30:09 GMT',
        'server': 'nginx',
        'vary': 'Accept-Encoding',
        'x-powered-by': 'PHP/7.0.30',
    }
    cookies = {
        'cookie': '_uab_collina=154057509277411566855101; Hm_lvt_2b441fdd1b590975e0e2d2a00d32226c=1540575093,1540767820; G1NZ_2132_pc_size_c=0; G1NZ_2132_sid=qYyU44; G1NZ_2132_saltkey=m1Hn9Uc1; G1NZ_2132_lastvisit=1540764547; G1NZ_2132_sendmail=1; Hm_lpvt_2b441fdd1b590975e0e2d2a00d32226c=1540768229; G1NZ_2132_seccode=4.8b84fc2ed99031ebbf; G1NZ_2132_lastact=1540768231%09plugin.php%09; G1NZ_2132_ulastactivity=b2f0C0r6c2CEv8vo4wkSbH%2Bsmz9yHN%2BTyg986PvAaeRw3fqswZGt; G1NZ_2132_auth=8abeTDpEsFXNRUbVxExfK8EpaxOanh39svtyFYtv08f%2BkkL1kwnW%2BOZ82KaDdauRNhMKhwEoZYKsHc5KNMG%2B7N1nGQ; G1NZ_2132_lastcheckfeed=16919%7C1540768231; G1NZ_2132_checkfollow=1; G1NZ_2132_lip=110.52.132.133%2C1540767822; G1NZ_2132_myrepeat_rr=R0; G1NZ_2132_dsu_amupper=DQo8c3R5bGU%2BDQoucHBlcndibSB7cGFkZGluZzo2cHggMTJweDtib3JkZXI6MXB4IHNvbGlkICNDRENEQ0Q7YmFja2dyb3VuZDojRjJGMkYyO2xpbmUtaGVpZ2h0OjEuOGVtO2NvbG9yOiMwMDMzMDA7d2lkdGg6MjAwcHg7b3ZlcmZsb3c6aGlkZGVufQ0KLnBwZXJ3Ym0gLnRpbWVze2NvbG9yOiNmZjk5MDA7fQ0KLnBwZXJ3Ym0gIGF7ZmxvYXQ6cmlnaHQ7Y29sb3I6I2ZmMzMwMDt0ZXh0LWRlY29yYXRpb246bm9uZX0NCjwvc3R5bGU%2BDQoNCjxkaXYgY2xhc3M9InBwZXJ3Ym0iIGlkPSJwcGVyd2JfbWVudSIgc3R5bGU9ImRpc3BsYXk6IG5vbmUiID4NCjxBIEhSRUY9InBsdWdpbi5waHA%2FaWQ9ZHN1X2FtdXBwZXI6cHBlcmxpc3QiIHRhcmdldD0iX2JsYW5rIj7mn6XnnIvnrb7liLDmjpLooYw8L0E%2BDQo8c3Ryb25nPue0r%2BiuoeetvuWIsDxzcGFuIGNsYXNzPSJ0aW1lcyI%2BMTA5PC9zcGFuPuasoTwvc3Ryb25nPjxicj4NCg0KPHN0cm9uZz7ov57nu63nrb7liLA8c3BhbiBjbGFzcz0idGltZXMiPjA8L3NwYW4%2B5qyhPC9zdHJvbmc%2BPGJyPg0KDQo8c3Ryb25nPuS4iuasoeetvuWIsDogPHNwYW4gY2xhc3M9InRpbWVzIj4yMDE4LTEwLTI5IDA3OjAzOjQ4PC9zcGFuPjwvc3Ryb25nPg0KPC9kaXY%2BDQo%3D'}  # 这里就是利用上面的函数获得的Cookies
    html = s.get(url,cookies=cookies,headers=header)
    print(html)
    soup=BeautifulSoup(html.text,"lxml")
    title=soup.select('tbody > tr > th > a.s.xst')
    print(type(title))
    for i in title:
        i=str(i)
        i=re.sub('(amp;)','',i)
        print(i)
        f.write(i+'\n')
for i in range(1,210):
    url = "https://www.kxdao.net/forum.php?mod=forumdisplay&fid=38&page={}".format(str(i))
    get_a(url)
f.close()



