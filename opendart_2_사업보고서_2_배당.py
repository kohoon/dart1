import requests as rq
from bs4 import BeautifulSoup

crtfc_key = '25320e73e479a8e8b9dcfa7a5a76faf0233652b5'
corp_code = '00126380' # 고유번호(주식코드 불가)
bsns_year = '2015'
reprt_code = '11011'
# dart_url = 'https://opendart.fss.or.kr/api/alotMatter.xml?crtfc_key='+crtfc_key+'&corp_code='+corp_code+'&bsns_year='+bsns_year+'&reprt_code='+reprt_code
dart_url = 'https://opendart.fss.or.kr/api/alotMatter.xml?crtfc_key='+crtfc_key+'&corp_code='+corp_code+'&bsns_year='+bsns_year+'&reprt_code='+reprt_code
res = rq.get(dart_url)
res2 = res.content.decode('utf-8')
soup = BeautifulSoup(res2, "lxml")

print(type(res2))
print(type(soup))
print(res2)